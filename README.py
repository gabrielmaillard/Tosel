import os
import urllib.parse

def generate_readme():
    exercises_folder = "Exercices"
    readme_content = ""

    exercise_files = []

    for filename in os.listdir(exercises_folder):
        if filename.endswith(".JPG"):
            exercise_files.append(filename)

    sorted_exercise_files = sorted(exercise_files, key=lambda x: int(x.split(" ")[1].split(".")[0]))

    for filename in sorted_exercise_files:
        exercise_number = filename.split(" ")[1].split(".")[0]
        exercise_title = f"### Exercice {exercise_number}\n"
        exercise_image_url = urllib.parse.quote(f"Exercices/{filename}")
        exercise_image = f"![Exercice {exercise_number}](Exercices/{exercise_image_url})\n"
        readme_content += exercise_title + exercise_image

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

generate_readme()
