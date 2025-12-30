from __future__ import annotations

import re
from pathlib import Path
import fitz  # PyMuPDF

PDF_PATH = Path("docs/source_pdfs/troubleshooting_guide.pdf")
OUTPUT_ROOT = Path("docs/extracted_md")


# Lines we want to drop anywhere (headers/footers). Keep these conservative.
DROP_LINE_PATTERNS = [
    r"^\s*UNCONTROLLED WHEN PRINTED\s*$",
    r"^\s*McDermott Aviation\s*$",
    r"^\s*Fire Fighting Tank\s*$",
    r"^\s*Doc No:\s*McDav-FFTTG\s*$",
    r"^\s*Revision:\s*\d+\s*$",
    r"^\s*Date:\s*\d{1,2}/\d{1,2}/\d{2,4}\s*$",
    r"^\s*Page\s+\d+\s+of\s+\d+\s*$",
    r"^\s*Third Revision\s*$",
]


def clean_page_text(text: str) -> str:
    # Normalize newlines
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    cleaned_lines: list[str] = []
    for line in text.splitlines():
        stripped = line.rstrip()

        # Drop known header/footer lines safely
        if any(re.match(pat, stripped, flags=re.IGNORECASE) for pat in DROP_LINE_PATTERNS):
            continue

        cleaned_lines.append(stripped)

    # Collapse excessive blank lines (keep at most 2)
    out = "\n".join(cleaned_lines)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.strip()


def extract_pages(doc: fitz.Document, start_page: int, end_page: int) -> str:
    """
    start_page and end_page are 1-based and inclusive.
    """
    if start_page < 1 or end_page < start_page or end_page > doc.page_count:
        raise ValueError(
            f"Invalid page range {start_page}-{end_page} for doc with {doc.page_count} pages"
        )

    parts: list[str] = []
    for p in range(start_page - 1, end_page):
        page = doc.load_page(p)
        page_text = page.get_text("text")
        page_text = clean_page_text(page_text)

        parts.append(f"\n\n<!-- PAGE:{p+1} -->\n\n")
        parts.append(page_text)
        parts.append("\n")

    # Final cleanup across whole doc (only whitespace)
    combined = "".join(parts)
    combined = re.sub(r"\n{3,}", "\n\n", combined).strip() + "\n"
    return combined


def write_markdown(out_path: Path, title: str, source_pages: str, body: str) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    md = []
    md.append(f"# {title}\n\n")
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

    start_page = 17
    end_page = 29
    body = extract_pages(doc, start_page=start_page, end_page=end_page)

    write_markdown(
        out_path=OUTPUT_ROOT / "02_thorough_checks" / "snorkel_pump_wont_operate" / "00_overview.md",
        title="Snorkel Pump Won’t Operate",
        source_pages=f"{start_page}–{end_page}",
        body=body,
    )


if __name__ == "__main__":
    main()
