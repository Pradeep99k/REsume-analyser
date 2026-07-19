skills = [
    "python",
    "Java",
    "SQL",
    "html",
    "CSS",
    "JavaScript",
    "Flask",
    "Machine Learning",
]
def extract_skills(text):
    text = text.lower()
    found=[]
    for skill in skills:
        if skill in text:
            found.append(skill)

    return found