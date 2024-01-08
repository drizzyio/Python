import fitz  # PyMuPDF


def pdf_to_text(pdf_path):
    try:
        with fitz.open(pdf_path) as pdf_document:
            text = ''
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                text += page.get_text()
        return text
    except FileNotFoundError:
        print(f"Error: The file '{pdf_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def save_text_to_file(text, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text saved to '{output_file}'.")
    except Exception as e:
        print(f"Error: Unable to save text to file. {e}")


if __name__ == "__main__":
    # Update the pdf_path with the correct file extension (.pdf)
    pdf_path = r'Input Path to PDF Here'

    # Output file path including the file name
    output_file_path = r'Input the path of the output file here'

    pdf_text = pdf_to_text(pdf_path)

    if pdf_text:
        save_text_to_file(pdf_text, output_file_path)
