from fpdf import FPDF
from PIL import Image
import os

def convert_file_to_pdf(file_path, filename):
    """
    Converts an image or document to a PDF.
    :param file_path: Path to the input file
    :param filename: The original file name
    :return: Path to the generated PDF or None if failed
    """
    try:
        # Determine the file extension
        extension = filename.rsplit('.', 1)[1].lower()

        # PDF Output Path
        pdf_filename = f"{filename.rsplit('.', 1)[0]}.pdf"
        pdf_path = os.path.join(os.getcwd(), 'output', pdf_filename)

        if extension in ['png', 'jpg', 'jpeg']:
            # Convert image to PDF
            image_to_pdf(file_path, pdf_path)
        elif extension in ['txt', 'doc', 'docx']:
            # Handle document conversion (txt to PDF for this example)
            text_to_pdf(file_path, pdf_path)
        else:
            return None

        return pdf_path

    except Exception as e:
        print(f"Error during file conversion: {e}")
        return None

def image_to_pdf(image_path, output_pdf_path):
    """
    Converts an image to PDF using Pillow (PIL).
    :param image_path: Path to the image
    :param output_pdf_path: Output path for the generated PDF
    """
    image = Image.open(image_path)
    image = image.convert('RGB')  # Convert to RGB mode if necessary
    image.save(output_pdf_path)

def text_to_pdf(text_file_path, output_pdf_path):
    try:
        """
        Converts a text file to a simple PDF using FPDF.
        :param text_file_path: Path to the text file
        :param output_pdf_path: Output path for the generated PDF
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        with open(text_file_path, 'r') as file:
            for line in file:
                pdf.cell(200, 10, txt=line, ln=True, align='L')

        pdf.output(output_pdf_path)
    except Exception as err:
        print(err)
        return err

