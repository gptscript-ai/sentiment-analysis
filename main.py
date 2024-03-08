import sys
from pypdf import PdfReader

pdf_file_path = sys.argv[1]
output_file_path = "content.txt"

reader = PdfReader(pdf_file_path)

with open(output_file_path, "w") as output_file:
    for page in reader.pages:
        text = page.extract_text()
        if text:
            output_file.write(text)
            output_file.write("\n")