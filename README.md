📄 Resume vs Job Description Matcher

A Python-based web application that analyzes how closely a candidate's resume matches a given Job Description (JD) using TF-IDF (Term Frequency–Inverse Document Frequency) and Cosine Similarity.

The application allows users to upload their resumes in PDF or DOCX format and paste a job description to calculate a matching score. It also identifies important keywords that are present or missing in the resume, helping candidates understand where their resumes can be improved.

🚀 Features

Resume Upload: Upload resumes in PDF or DOCX format.

Job Description Input: Paste the job description directly into the application.

Match Score Calculation: Calculates resume–JD similarity using TF-IDF and Cosine Similarity.

Matched Keywords: Displays important job-related keywords already present in the resume.

Missing Keywords: Identifies important keywords from the job description that are missing from the resume.

Interactive Interface: Simple and user-friendly interface built with Streamlit.

Text Preprocessing: Converts text to lowercase, removes unnecessary characters, and eliminates extra whitespace.

🛠️ Technologies Used

Technology

Purpose

Python

Core programming language

Streamlit

Web application interface

Scikit-learn

TF-IDF vectorization and Cosine Similarity

PDFPlumber

Extracting text from PDF resumes

Python-docx

Extracting text from DOCX resumes

Regular Expressions (RE)

Text cleaning and preprocessing

📂 Project Structure

Resume-JD-Matcher/
│
├── app.py              # Main Streamlit application
├── utils.py            # Text extraction, preprocessing and analysis
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation

⚙️ How It Works

The project follows a simple text-processing and similarity-analysis pipeline.

1. Resume Upload

The user uploads a resume in PDF or DOCX format.

PDFPlumber extracts text from PDF files.

Python-docx extracts text from DOCX files.

2. Job Description Input

The user pastes the target job description into the provided text area.

3. Text Preprocessing

Both the resume text and job description undergo preprocessing:

Convert all text to lowercase.

Remove numbers and special characters.

Remove unnecessary whitespace.

Normalize the text for further analysis.

4. TF-IDF Vectorization

TF-IDF converts the processed text into numerical vectors based on the importance of words.

It considers:

Term Frequency (TF): How frequently a word appears in a document.

Inverse Document Frequency (IDF): How important or unique a word is across the documents.

5. Cosine Similarity

Cosine Similarity measures the similarity between the resume and job description vectors.

The similarity score is converted into a percentage.

Formula:

Cosine Similarity = (A · B) / (||A|| × ||B||)

Where:

A = Resume TF-IDF vector

B = Job Description TF-IDF vector

A · B = Dot product of the two vectors

||A|| and ||B|| = Magnitudes of the vectors

6. Keyword Analysis

The application extracts the top 25 important keywords from the job description using TF-IDF.

It then compares these keywords with the words present in the resume and separates them into:

Matched Keywords: Keywords found in the resume.

Missing Keywords: Keywords not found in the resume.

7. Result Display

The application displays the final similarity score along with matched and missing keywords.

📊 Match Score Interpretation

Match Score

Interpretation

75% – 100%

Strong Fit

50% – 74.99%

Decent Match – Can Be Improved

Below 50%

Low Similarity – Resume Needs Tailoring

The score represents textual similarity, not a guaranteed ATS score or prediction of recruitment success.

💻 Installation and Setup

Follow these steps to run the project locally.

Prerequisites

Python 3.9 or above

pip (Python package manager)

VS Code or any Python IDE

Step 1: Clone the Repository

git clone https://github.com/your-username/Resume-JD-Matcher.git

Step 2: Navigate to the Project Directory

cd Resume-JD-Matcher

Step 3: Create a Virtual Environment (Optional)

python -m venv venv

Activate it:

Windows:

venv\Scripts\activate

Linux / macOS:

source venv/bin/activate

Step 4: Install Dependencies

pip install -r requirements.txt

Step 5: Run the Application

streamlit run app.py

The application will open automatically in your browser.

If it doesn't, open:

http://localhost:8501

📦 Requirements

Create a requirements.txt file containing:

streamlit
pdfplumber
python-docx
scikit-learn

🖥️ Application Workflow

Open the application.

Upload your resume (PDF or DOCX).

Paste the job description into the text area.

Click Calculate Match Score.

View the overall resume–JD matching percentage.

Review matched keywords.

Identify missing keywords and improve your resume where relevant.

🔮 Future Improvements

Some potential improvements for future versions include:

Integration of advanced NLP techniques.

Semantic similarity using Sentence-BERT or other transformer models.

Support for additional resume formats.

Automatic resume improvement suggestions.

Job description recommendations based on candidate skills.

Resume section-wise analysis.

Integration with online job portals.

Downloadable resume analysis reports.

⚠️ Limitations

The application currently supports only PDF and DOCX resumes.

Similarity is based on textual and keyword similarity rather than semantic understanding.

The keyword analysis considers the top 25 important JD keywords.

Different wording for similar skills may not be recognized as a match.

A high similarity score does not guarantee selection or recruitment success.

👨‍💻 Author
