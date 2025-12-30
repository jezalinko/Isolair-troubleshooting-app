from __future__ import annotations
import re
from pathlib import Path
import fitz  # PyMuPDF

PDF_PATH = Path("docs/source_pdfs/troubleshooting_guide.pdf")
OUTPUT_ROOT = Path("docs/extracted_md")

def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"UNCONTROLLED WHEN PRINTED.*?Fire Fighting Tank", "", text, flags=re.S)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = "\n".join(line.rstrip() for line in text.splitlines())
    return text.strip() + "\n"

def extract_pages(doc: fitz.Document, start_page: int, end_page: int) -> str:
    if start_page < 1 or end_page < start_page or end_page > doc.page_count:
        raise ValueError(f"Invalid page range {start_page}-{end_page} for doc with {doc.page_count} pages")

    parts: list[str] = []
    for p in range(start_page - 1, end_page):
        parts.append(f"\n\n--- PAGE {p+1} ---\n\n")
        page = doc.load_page(p)
        parts.append(page.get_text("text"))

    return clean_text("".join(parts))

def write_markdown(out_path: Path, title: str, source_pages: str, body: str) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    md = []
    md.append(f"# {title}\n")
    md.append(f"**Source:** `{PDF_PATH.as_posix()}`  \n")
    md.append(f"**Pages:** {source_pages}\n")
    md.append("\n---\n\n")
    md.append(body)

    out_path.write_text("".join(md), encoding="utf-8")
    print(f"Wrote: {out_path}  ({len(body)} chars)")

def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"PDF not found at {PDF_PATH.resolve()}")

    doc = fitz.open(str(PDF_PATH))

    body = extract_pages(doc, start_page=17, end_page=30)

    write_markdown(
        out_path=OUTPUT_ROOT / "02_thorough_checks" / "leaking_doors" / "00_overview.md",
        title="Leaking Doors",
        source_pages="67",
        body=body,
    )

if __name__ == "__main__":
    main()

