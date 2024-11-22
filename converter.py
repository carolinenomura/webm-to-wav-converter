import os
import ffmpeg
import tkinter as tk
from tkinter import filedialog

def convert_audio(input_file, output_file):
    try:
        ffmpeg.input(input_file).output(output_file).run(cmd='ffmpeg.exe')
        print(f"O arquivo {input_file} foi convertido para {output_file} com sucesso")
    except ffmpeg.Error as e:
        print(f"Erro ao converter o arquivo {input_file}: {e.stderr.decode()}")

def convert_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    webm_files = [f for f in os.listdir(input_folder) if f.endswith(".webm")]

    if not webm_files:
        print("Não existe nenhum arquivo .webm na pasta selecionada")
        return
    
    for file_name in webm_files:
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".wav")
        convert_audio(input_file, output_file)
    print("Conversão de todos os áudios finalizada com êxito!")

def select_folder(title):
    root = tk.Tk()
    root.withdraw() 
    folder = filedialog.askdirectory(title=title)
    return folder

def main():
    print("Selecionar pasta com os arquivos de áudio webm para conversão...")
    input_folder = select_folder("Selecionar pasta com os arquivos de áudio webm para conversão")
    if not input_folder:
        print("Nenhuma pasta foi selecionada. Encerrando...")
        return
    
    print("Selecionar pasta onde serão salvos os áudios convertidos para wav...")
    output_folder = select_folder("Selecionar pasta onde serão salvos os áudios convertidos para wav")
    if not output_folder:
        print("Nenhuma pasta foi selecionada. Encerrando...")
        return

    convert_folder(input_folder, output_folder)

if __name__ == "__main__":
    main()