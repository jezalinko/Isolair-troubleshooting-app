from __future__ import annotations

import re
from pathlib import Path
import fitz  # PyMuPDF


PDF_PATH = Path("docs/source_pdfs/troubleshooting_guide.pdf")
OUTPUT_ROOT = Path("docs/extracted_md")

def clean_text(text: str) -> str:
    # Normalize whitespace a bit without destroying tables too much
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # Remove excessive blank lines (keep at most 2)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Trim trailing spaces on each line
    text = "\n".join(line.rstrip() for line in text.splitlines())
    return text.strip() + "\n"

def extract_pages(doc: fitz.Document, start_page: int, end_page: int) -> str:
    """
    start_page and end_page are 1-based and inclusive (human-friendly).
    """
    if start_page < 1 or end_page < start_page or end_page > doc.page_count:
        raise ValueError(f"Invalid page range {start_page}-{end_page} for doc with {doc.page_count} pages")

    parts: list[str] = []
    for p in range(start_page - 1, end_page):  # convert to 0-based
        page = doc.load_page(p)
        # "text" is usually best for documents; "blocks" can be used later for better structure
        parts.append(page.get_text("text"))
    return clean_text("\n\n---\n\n".join(parts))

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

    # ✅ Start with ONE section to prove the pipeline works.
    # You said “First Checks pages 13–16” (human page numbers).
    body = extract_pages(doc, start_page=13, end_page=16)
    write_markdown(
        out_path=OUTPUT_ROOT / "01_first_checks" / "00_first_checks_pages_13-16.md",
        title="First Checks (Troubleshooting Matrix)",
        source_pages="13–16",
        body=body,
    )

if __name__ == "__main__":
    main()
