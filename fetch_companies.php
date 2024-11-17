<?php
header("Content-Type: application/json");
$data = json_decode(file_get_contents("php://input"));

$jobTitle = $data->job_title;
$experience = $data->experience;

$pdo = new PDO('mysql:host=localhost;dbname=jobnest', 'root');
$query = $pdo->prepare("SELECT * FROM companies");
$query->execute();
$companies = $query->fetchAll(PDO::FETCH_ASSOC);

$body = json_encode(["companies" => $companies, "user_job_title" => $jobTitle, "user_experience" => $experience]);

$context = stream_context_create([
    "http" => [
        "method" => "POST",
        "header" => "Content-Type: application/json\r\n",
        "content" => $body,
    ]
]);

$pythonResponse = @file_get_contents("http://localhost:8000/rank_companies", false, $context);

// Handle errors in the request
if ($pythonResponse === FALSE) {
    $error = error_get_last();
    echo json_encode(["error" => "Unable to connect to Python API", "details" => $error]);
    exit;
}

$rankedCompanies = json_decode($pythonResponse, true);
echo json_encode($rankedCompanies);

?>