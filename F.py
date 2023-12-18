import os
import tempfile
from pdf2image import convert_from_path
from pathlib import Path
from shutil import rmtree
import tkinter as tk
from tkinter import filedialog
import seaborn as sns
import torch

def verify_directory(chat_id):
    chat_ID = str(chat_id)
    pdf_path = Path(f"./PDFs/{chat_ID}")
    return pdf_path.exists() and any(pdf_path.glob("*.pdf"))

def create_directory(chat_id):
    chat_ID = str(chat_id)
    image_dir = Path(f"ID}")
    image_dir.mkdir(parents=True, exist_ok=True)
    return str(image_dir)

def convert_pdf_to_images(chat_id):
    pdf_path = list_PDF(chat_id)
    with tempfile.TemporaryDirectory() as temp_dir:
        images_from_path = convert_from_path(pdf_path, output_folder=temp_dir)
    save_dir = create_directory(chat_id)
    for i, page in enumerate(images_from_path, start=1):
        if i <= 10:
            base_file_name = f"{i}.jpg"
            page.save(pathx.join(save_dir, base_file_name), "JPEG")
        else:
            print("Limit for extraction is 10 images")

def list_images(chat_id):
   
    image_path = Path(f".")
  
    images = [str(img_path) for img_path in sorted(image_path.glob("*.jpg"))][:10]
    return images

def delete_all_images(chat_id):
    image_path = Path(f"./images/{chat_id}")
    rmtree(image_path)

def generate_torch_tensor():
    torch_tensor = torch.randn(100)
    return torch_tensor

def display_seaborn_plot():
    
    sns.lineplot(x=range(10), y=range(10))
    plt.show()

def select_pdf_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    pdf_file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return pdf_file_path


chat_id = 123
if verify_directory(chat_id):
    convert_pdf_to_images(chat_id)
    image_list = list_images(chat_id)
    print("List of Images:", image_list)

 asks
    torch_tensor = generate_torch_tensor()
    print("Torch Tensor:", torch_tensor)

    display_seaborn_plot()

  
    selected_pdf = select_pdf_file()
    print("Selected PDF:", selected_pdf)

    delete_all_images(chat_id)
