import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle

# Improved sample data with detailed experience suitability scenarios
data = pd.DataFrame(
    {
        "user_job_title": [
            "Software Engineer",
            "Data Scientist",
            "Web Developer",
            "Project Manager",
            "Mobile App Developer",
            "Cloud Engineer",
            "Machine Learning Engineer",
            "Cybersecurity Analyst",
            "UI/UX Designer",
            "DevOps Engineer",
            "Backend Developer",
            "Frontend Developer",
            "Product Manager",
            "Database Administrator",
            "AI Specialist",
        ],
        "user_experience": [2, 3, 1, 5, 4, 6, 2, 3, 1, 4, 2, 1, 7, 5, 3],
        "company_job_title": [
            "Backend Developer",  # Matches but experience is lower
            "Data Scientist",  # Matches perfectly
            "Frontend Developer",  # Matches perfectly
            "Project Manager",  # Matches perfectly
            "Mobile Developer",  # Matches perfectly
            "Cloud Architect",  # Overqualified
            "AI Engineer",  # Matches perfectly
            "Information Security Analyst",  # Matches perfectly
            "Graphic Designer",  # Mismatch
            "Site Reliability Engineer",  # Matches perfectly
            "Backend Developer",  # Matches perfectly
            "Web Developer",  # Underqualified
            "Senior Product Manager",  # Overqualified
            "Database Engineer",  # Matches but less experience
            "AI Researcher",  # Matches perfectly
        ],
        "company_required_experience": [3, 3, 1, 5, 4, 5, 2, 3, 2, 4, 2, 2, 6, 6, 3],
        "suitability": [
            0,  # Experience too low (2 vs. required 3)
            1,  # Perfect match
            1,  # Perfect match
            1,  # Perfect match
            1,  # Perfect match
            0,  # Overqualified (6 vs. required 5)
            1,  # Perfect match
            1,  # Perfect match
            0,  # Mismatch (UI/UX Designer vs. Graphic Designer)
            1,  # Perfect match
            1,  # Perfect match
            0,  # Underqualified (1 vs. required 2)
            0,  # Overqualified (7 vs. required 6, senior role mismatch)
            0,  # Experience too low (5 vs. required 6)
            1,  # Perfect match
        ],
    }
)

# Split features and target
X = data[
    [
        "user_job_title",
        "user_experience",
        "company_job_title",
        "company_required_experience",
    ]
]
y = data["suitability"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Preprocessing: Vectorize both job titles and scale both experience values
preprocessor = ColumnTransformer(
    transformers=[
        ("user_title", TfidfVectorizer(), "user_job_title"),
        ("company_title", TfidfVectorizer(), "company_job_title"),
        (
            "user_experience",
            StandardScaler(),
            ["user_experience"],
        ),  # Wrap in list to keep as 2D
        (
            "company_experience",
            StandardScaler(),
            ["company_required_experience"],
        ),  # Wrap in list to keep as 2D
    ]
)

# Build the pipeline with a classifier (e.g., Random Forest)
pipeline = make_pipeline(preprocessor, RandomForestClassifier())

# Train the model
pipeline.fit(X_train, y_train)

# Save the trained model to a file
with open("ml_model.pkl", "wb") as model_file:
    pickle.dump(pipeline, model_file)

print("Model training complete and saved as 'ml_model.pkl'")
