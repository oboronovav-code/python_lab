import random
def generate_grades(count):
    grades = []

    for i in range(count):
        grade = random.randint(1,12)
        grades.append(grade)

    return grades

def average_grade(grades):
    return sum(grades) / len(grades)

def get_level(average):
    if average >= 10 and average <= 12:
        return "Високий"
    elif average >= 7:
        return "Достатній"
    elif average >= 4:
        return "Середній"
    else:
        return "Низький"