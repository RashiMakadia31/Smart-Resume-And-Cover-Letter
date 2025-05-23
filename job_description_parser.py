import docx2txt
import PyPDF2

def parse_job_description(file):
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = " ".join(page.extract_text() for page in reader.pages)
    elif file.name.endswith(".docx"):
        text = docx2txt.process(file)
    elif file.name.endswith(".txt"):
        text = file.read().decode("utf-8")
    else:
        text = ""

    # Extract skills heuristically
    skills = [word.strip().lower() for word in text.split() if word.lower() in {"python", "sql", "ml", "communication", "leadership", "aws"}]
    return text, skills
