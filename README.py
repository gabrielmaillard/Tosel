import os
import urllib.parse
import subprocess

def push():
    repository_directory = os.getcwd()

    subprocess.run(["git", "add", "*"], cwd=repository_directory)
    subprocess.run(["git", "commit", "-m", "New exercises"], cwd=repository_directory)
    subprocess.run(["git", "push"], cwd=repository_directory)

def generate_readme(FILE):
    header = 'Ce fichier a été généré et envoyé automatiquement à partir du script python intitulé "README.py".\nL\'exercice 14 est accompagné d\'un script. (cf. Exercice 14.py)\n\n'

    with open(FILE, "w") as readme_file:
        readme_file.write(header)
        readme_file.write(insert_exercises(FILE))

def insert_exercises(FILE):
    exercises_folder = "Exercices"
    readme_content = ""

    exercises = {}

    for filename in os.listdir(exercises_folder):
        if filename.endswith(".JPG"):
            exercise_number = filename.split(" ")[1].split(".")[0]
            if exercise_number not in exercises:
                exercises[exercise_number] = []
            exercises[exercise_number].append(filename)
    
    for exercise_number, filenames in sorted(exercises.items(), key=lambda x: int(x[0])):
        readme_content += f"[Exercice {exercise_number}](#exercice{exercise_number})\n"

    readme_content += "\n\n\n"

    for exercise_number, filenames in sorted(exercises.items(), key=lambda x: int(x[0])):
        exercise_title = f"\n### Exercice {exercise_number}\n"
        exercise_images = ""
        for filename in filenames:
            exercise_image_url = urllib.parse.quote(f"Exercices/{filename}")
            exercise_images += f"![Exercice {exercise_number}]({exercise_image_url})\n"
        readme_content += exercise_title + exercise_images

    return readme_content

generate_readme("README.md")
push()