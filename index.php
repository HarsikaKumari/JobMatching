<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Matching Application</title>
</head>

<body>
    <h1>Find Companies for Your Job Title and Experience</h1>
    <form id="job-form">
        <label for="job_title">Job Title:</label>
        <input type="text" id="job_title" name="job_title" required><br><br>
        <label for="experience">Years of Experience:</label>
        <input type="number" id="experience" name="experience" required><br><br>
        <button type="submit">Search</button>
    </form>
    <div id="result"></div>

    <script>
        document.getElementById('job-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const jobTitle = document.getElementById('job_title').value;
            const experience = document.getElementById('experience').value;

            // Structure the request data as per your requirement
            const requestData = {
                job_title: jobTitle,
                experience: parseInt(experience),
            };

            const response = await fetch('fetch_companies.php', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestData)
            });

            let output = "<h2>Recommended Companies:</h2><ul>";

            const companies = await response.json();
            console.log(companies);
            companies.forEach(company => {
                output += `<li>${company.company_name} - ${company.location || "Not Provided"}</li>`;
            });

            output += "</ul>";
            document.getElementById('result').innerHTML = output;
        });
    </script>
</body>

</html>