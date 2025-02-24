import exifread
import os

def get_exif_data(image_path):
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)
        
        if tags:
            exif_data = {tag: str(value) for tag, value in tags.items()}
            return exif_data
        else:
            return "Nessun dato EXIF trovato."

image_path = "focal_example.jpg"

if not os.path.exists(image_path):
    print("Errore: Il file non esiste!")
else:
    print(get_exif_data(image_path))

