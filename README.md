# JobMatching

**JobMatching** is a web-based platform designed to connect job seekers with relevant job opportunities. This project aims to simplify the job application process by providing a user-friendly interface for browsing, filtering, and applying for jobs. 

## Features

- **User Registration and Login**: Secure authentication for both job seekers and recruiters.
- **Job Listings**: Recruiters can post job openings with detailed descriptions.
- **Search and Filter**: Users can search and filter jobs based on criteria like location, job type, and skills.
- **Profile Management**: Job seekers can create and update their profiles, including skills and resume uploads.
- **Application Tracking**: Allows users to track the status of their job applications.

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: PHP
- **Database**: MySQL
- **Other Tools**: Git for version control

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HarsikaKumari/JobMatching.git
   ```
2. Navigate to the project directory:
   ```bash
   cd JobMatching
   ```
3. Set up the database:
   - Import the provided SQL file into your MySQL database.
   - Update the database credentials in the fetch_companies file (`fetch_companies.php`).

4. Run the application:
   - Host the project locally using a server like XAMPP or WAMP.

## Project Structure

```plaintext
JobMatching/
├── app.py
├── index.php        # Home page
├── fetch_companies.php
├── command. md
├── ml_model.pkl
├── requirements.txt
├── training.py
└── README.md        # Project documentation
```

## How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).
