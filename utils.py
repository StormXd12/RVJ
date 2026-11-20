import re
import pdfplumber
import docx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_text_from_docx(uploaded_file):
    document = docx.Document(uploaded_file)
    text = "\n".join(para.text for para in document.paragraphs)
    return text


def extract_resume_text(uploaded_file):
 
    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")


def clean_text(text):

    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def compute_similarity_score(resume_text, jd_text):
 
    documents = [resume_text, jd_text]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    score = round(similarity * 100, 2)
    return score


def get_keyword_analysis(resume_text, jd_text, top_n=25):
   
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([jd_text])
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]

    # Sort JD keywords by importance (TF-IDF score), descending
    keyword_scores = sorted(zip(feature_names, scores), key=lambda x: x[1], reverse=True)
    top_keywords = [kw for kw, score in keyword_scores[:top_n] if score > 0]

    resume_words = set(resume_text.split())

    matched_keywords = [kw for kw in top_keywords if kw in resume_words]
    missing_keywords = [kw for kw in top_keywords if kw not in resume_words]

    return matched_keywords, missing_keywords
