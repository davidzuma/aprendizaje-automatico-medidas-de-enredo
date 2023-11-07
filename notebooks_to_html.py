import subprocess
import os


def notebooks_in_folder_to_html(input_folder_name: str, output_folder_name: str) -> None:
    files = os.listdir(input_folder_name)
    for file in files:
        input_path = os.path.join(input_folder_name, file)
        output_path = os.path.join(output_folder_name, file.split(".")[0])
        notebook_to_html(input_path, output_path)


def notebook_to_html(notebook_path: str, output_path: str) -> None:
    subprocess.run([f"jupyter nbconvert --to html {notebook_path} --output {output_path}"], shell=True, text=True)


if __name__ == "__main__":
    current_path = os.getcwd()
    input_folder_name = os.path.join(current_path, "notebooks/aprendizaje_supervisado")
    output_folder_name = os.path.join(current_path, "docs/aprendizaje_supervisado")
    notebooks_in_folder_to_html(input_folder_name, output_folder_name)
