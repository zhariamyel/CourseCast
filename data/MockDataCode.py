import random
import pandas as pd


courses = [
 ("CHEM1150", "General Chemistry I", "Chemistry", 100),
    ("CHEM1151", "General Chemistry I Lab", "Chemistry", 100),
    ("CHEM1160", "General Chemistry II", "Chemistry", 100),
    ("MATH1100", "College Algebra", "Mathematics", 100),
    ("BIOL1100", "Principles of Biology", "Biology", 100),
    ("BIOL1200", "Principles of Biology II", "Biology", 200),
    ("PHYS1010", "Introductory Physics I", "Physics", 100),
    ("PHYS1020", "Introductory Physics II", "Physics", 100),
    ("ENGL1200", "English Composition II", "English", 100),
    ("HIST1110", "World Civilization I", "History", 100),
    ("HIST1120", "World Civilization II", "History", 100),
    ("PSYC1000", "Introduction to Psychology", "Psychology", 100),
    ("SOCI2000", "Introduction to Sociology", "Sociology", 200),
    ("ACCT2010", "Principles of Accounting I", "Business", 200),
    ("ACCT2020", "Principles of Accounting II", "Business", 200),
    ("ECON2010", "Principles of Microeconomics", "Economics", 200),
    ("ECON2020", "Principles of Macroeconomics", "Economics", 200),
    ("COMM1000", "Fundamentals of Speech", "Communication", 100),
    ("PHIL1010", "Introduction to Philosophy", "Philosophy", 100),
    ("SPAN1010", "Elementary Spanish I", "Languages", 100),
    ("CMST1010", "Fundamentals of Public Speaking", "Communication", 100),
    ("CPSC1005", "Intro to PCs and Software Applications", "Computer Science", 100),
    ("PSYC1010", "Introduction to Psychology", "Psychology", 100),
    ("CPSC1724", "Intro to Computer Science", "Computer Science", 100),
    ("ENGL1010", "English Composition and Rhetoric", "English", 100),
    ("FINC1070", "Personal Finance", "Finance", 100),
    ("HIST1030", "World Civilizations to 1500", "History", 100),
    ("MATH1030I", "Intensive Precalculus", "Mathematics", 100),
    ("XCOR1000", "College Experience", "Core Experience", 100),
    ("CPSC2735", "Data Structures and Lab", "Computer Science", 200),
    ("ENGL1020", "English Composition and Literature", "English", 100),
    ("MATH1070", "Introductory Calculus", "Mathematics", 100),
    ("PHIL1040", "Happiness and the Meaning of Life", "Philosophy", 100),
    ("ART1010", "Design I", "Art", 100),
    ("CPSC2740", "Software Development", "Computer Science", 200),
    ("MSCM2590", "Black Cinema", "Media Studies", 200),
    ("PHIL2040", "Logic", "Philosophy", 200),
    ("STAT2010", "Statistical Methods I", "Mathematics", 200),
    ("THEO1100", "The Christian Faith", "Theology", 100),
    ("CPSC2120", "Computer Organization and Architecture", "Computer Science", 200),
    ("CPSC3710", "Database Systems", "Computer Science", 300),
    ("ENGL3185", "Black Hair Narratives", "English", 300),
    ("MATH2030", "Elementary Linear Algebra", "Mathematics", 200),
    ("MSCM2400", "Social Media", "Media Studies", 200),
    ("BIOL1030", "General Biology (Non-Science Major)", "Biology", 100),
    ("BIOL1030L", "General Biology Lab (Non-Science Major)", "Biology", 100),
    ("CPSC3140", "Operating Systems", "Computer Science", 300),
    ("CPSC3603", "Special Topics: Mobile App Development", "Computer Science", 300),
    ("MATH2550", "Discrete Structures for Computer Science", "Mathematics", 200),
    ("XCOR3010", "Dystopia, Real and Imagined", "Core Experience", 300),
    ("XCOR3020", "Afro-Latin America and LA Oral Traditions", "Core Experience", 300),
    ("CPSC3060", "Design and Analysis of Algorithms", "Computer Science", 300),
    ("CPSC3603", "Special Topics: Bioinformatics Computing", "Computer Science", 300),
    ("CPSC4800", "Capstone Project I", "Computer Science", 400),
    ("MGMT3160", "Project Management", "Business", 300),
    ("STAT2021", "Statistical Methods II", "Mathematics", 300),
    ("CPSC3603", "Special Topics: Data Analytics", "Computer Science", 300),
    ("CPSC3900", "Computer Science Internship I", "Computer Science", 300),
    ("ENGL4060S", "Black Gothic Literature", "English", 400),
    ("SPAN1010", "Elementary Spanish", "Languages", 100),
    ("AADS2000", "Introduction to African American History and Culture", "African American Studies", 200),
    ("ART2110", "History of Art I", "Art", 200),
    ("CHIN1010", "Elementary Chinese", "Languages", 100),
    ("CPSC4805", "Capstone Project II", "Computer Science", 400),
    ("CPSC4999", "Senior Comprehensives", "Computer Science", 400),
    ("CPSC4999P", "Senior Comprehensives Programming", "Computer Science", 400),
    ("XCOR3010", "Race, Culture, and Communication", "Core Experience", 300),
]

instructors = [  "Washington", "Jefferson", "Jackson", "Harris", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright",
    "Scott", "Torres", "Parker", "Evans", "Edwards",
    "Collins", "Stewart", "Morris", "Murphy", "Cook",
    "Bell", "Carter", "Phillips", "Campbell", "Mitchell",
    "Roberts", "Turner", "Phillips", "Brooks", "Gray",
    "Green", "Adams", "Nelson", "Baker", "Hall",
    "Johnson", "Williams", "Brown", "Davis", "Thomas",
    "Moore", "Taylor", "White", "Hughes", "Alexander"]

semesters = ["Fall", "Spring", "Fall", "Spring"]

year = [2022, 2023, 2023, 2024]

modalities = ["In-Person", "Online", "Hybrid"]


records = []

for course in courses:
    course_code, course_name, department, credits = course
    for semester in semesters:
        capacity = random.randint(30, 120)
        instructor = random.choice(instructors)
        enrollment = random.randint(10, 100)
        credits = random.randint(0, 5)

        records.append({
            "Course Code": course_code,
            "Course Name": course_name,
            "Department": department,
            "Credits": credits,
            "Semester": semester,
            "Year": random.choice(year),
            "Instructor": instructor,
            "Capacity": capacity,
            "Enrollment": enrollment,
            "Modalities": random.choice(modalities)
            
        })

df = pd.DataFrame(records)
df.to_csv("course_data.csv", index=False)

print("Sample course data generated and saved to course_data.csv")


