from flask import Flask, request, jsonify
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all domains
CORS(app, resources={r"/*": {"origins": "*"}})

# Load the trained model
with open("ml_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


@app.route("/rank_companies", methods=["POST"])
def rank_companies():
    data = request.json
    user_job_title = data["user_job_title"]
    user_experience = data["user_experience"]
    companies = data[
        "companies"
    ]  # List of companies with job title and experience requirements

    suitability_scores = []

    print(user_job_title, user_experience, companies)

    for company in companies:
        # Extract company job title and required experience
        company_job_title = company["required_job_title"]
        company_required_experience = company["required_experience"]

        # Prepare the data as a DataFrame with expected column names
        input_data = pd.DataFrame(
            [
                {
                    "user_job_title": user_job_title,
                    "user_experience": user_experience,
                    "company_job_title": company_job_title,
                    "company_required_experience": company_required_experience,
                }
            ]
        )

        # Predict suitability using user and company details
        prediction = model.predict_proba(input_data)[0][1]

        # Append the company with its suitability score
        suitability_scores.append(
            {
                "company_name": company["company_name"],
                "location": company["location"],
                "suitability_score": prediction,
            }
        )

    # Sort companies by suitability score in descending order
    sorted_companies = sorted(
        suitability_scores, key=lambda x: x["suitability_score"], reverse=True
    )

    return jsonify(sorted_companies)


if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0", debug=True)
