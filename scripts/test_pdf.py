import fitz
from pathlib import Path

pdf_path = Path("docs/source_pdfs/troubleshooting_guide.pdf")


print("Looking for PDF at:", pdf_path.resolve())
print("Exists:", pdf_path.exists())

doc = fitz.open(str(pdf_path))
print("Pages:", doc.page_count)

