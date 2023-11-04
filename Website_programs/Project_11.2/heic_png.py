from PIL import Image
import os

input_folder = "/Users/fradere/Documents/projects_dir/Project_11/Project_11.2/Foto_drop"
output_folder = "/Users/fradere/Documents/projects_dir/Project_11/Project_11.2/Foto_finali"

def convert_heic_to_png(input_file, output_folder):
    try:
        img = Image.open(input_file)
        filename = os.path.splitext(os.path.basename(input_file))[0] + ".png"
        output_file = os.path.join(output_folder, filename)

        img.save(output_file, "PNG")
        print(f"Conversione completata: {input_file} -> {output_file}")

    except Exception as e:
        print(f"Si è verificato un errore durante la conversione: {e}")

# Verifica che la cartella di destinazione esista, altrimenti creala
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Ciclo attraverso i file nella cartella di input
for filename in os.listdir(input_folder):
    if filename.endswith(".heic"):
        input_file = os.path.join(input_folder, filename)
        convert_heic_to_png(input_file, output_folder)
