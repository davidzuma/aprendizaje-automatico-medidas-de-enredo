import subprocess
import os
from typing import List


def create_index_file(file_names: List[str], output_folder: str):
    with open(f"{output_folder}/index.md", "w") as file:
        output_folder_name = output_folder.split("/")[-1]
        section_name = output_folder_name.replace("_", " ").capitalize()
        file.write(f"# {section_name}.En esta sección se ven conceptos de {section_name}.\n")
        for file_name in file_names:
            subsection_name = file_name.replace("_", " ").capitalize()
            file.write(f"- [{subsection_name}]({file_name}.html) \n")


def notebooks_in_folder_to_html(input_folder_name: str, output_folder_name: str) -> List[str]:
    files = os.listdir(input_folder_name)
    file_names = list()
    for file in files:
        input_path = os.path.join(input_folder_name, file)
        file_name = file.split(".")[0]
        output_path = os.path.join(output_folder_name, file_name)
        notebook_to_html(input_path, output_path)
        file_names.append(file_name)
    return file_names


def notebook_to_html(notebook_path: str, output_path: str) -> None:
    subprocess.run([f"jupyter nbconvert --to html {notebook_path} --output {output_path}"], shell=True, text=True)


if __name__ == "__main__":
    current_path = os.getcwd()
    folders = ["aprendizaje_supervisado", "aprendizaje_no_supervisado", "aprendizaje_profundo", "medidas_enredo"]
    for folder in folders:
        input_folder_name = os.path.join(current_path, f"notebooks/{folder}")
        output_folder_name = os.path.join(current_path, f"docs/{folder}")
        file_names = notebooks_in_folder_to_html(input_folder_name, output_folder_name)
        create_index_file(file_names, output_folder_name)
