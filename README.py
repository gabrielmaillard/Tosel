import os
import urllib.parse

def generate_readme():
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
        exercise_title = f"\n### Exercice {exercise_number}\n"
        exercise_images = ""
        for filename in filenames:
            exercise_image_url = urllib.parse.quote(f"Exercices/{filename}")
            exercise_images += f"![Exercice {exercise_number}](Exercices/{exercise_image_url})\n"
        readme_content += exercise_title + exercise_images

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

generate_readme()
