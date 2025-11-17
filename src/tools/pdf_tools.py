"""
PDF fetching and parsing tools for ResearchForge AI

This module provides a robust PDF downloader and text extractor used by
PaperAnalyzerAgent. It prefers PyMuPDF (fitz) for extraction and falls back
to PyPDF2 when necessary.
"""

import requests
import io
from typing import Dict
import PyPDF2
import fitz  # pymupdf - preferred for higher quality extraction


def fetch_pdf(url: str) -> Dict:
    """
    Fetches a PDF from a URL and extracts its text content.

    Args:
        url: Direct URL to a PDF file (e.g., arxiv.org, ACL anthology, etc.)

    Returns:
        dict: {
            "status": "success" | "error",
            "text": "extracted text content" | None,
            "page_count": int | None,
            "message": "error description if failed"
        }
    """
    try:
        # Step 1: Download the PDF
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()  # Raise exception for bad status codes

        # Verify it's actually a PDF
        content_type = response.headers.get('content-type', '').lower()
        if 'application/pdf' not in content_type and not url.lower().endswith('.pdf'):
            return {
                "status": "error",
                "text": None,
                "page_count": None,
                "message": f"URL does not point to a PDF file. Content-Type: {content_type}"
            }

        # Step 2: Extract text using PyMuPDF (better quality than PyPDF2)
        pdf_bytes = io.BytesIO(response.content)

        try:
            # Try PyMuPDF first (better quality)
            doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            text_parts = []
            page_count = len(doc)

            # Limit to first 50 pages to manage context size
            max_pages = min(page_count, 50)

            for page_num in range(max_pages):
                page = doc[page_num]
                text_parts.append(page.get_text())

            doc.close()
            extracted_text = "\n\n".join(text_parts)

        except Exception as pymupdf_error:
            # Fallback to PyPDF2 if PyMuPDF fails
            pdf_bytes.seek(0)  # Reset stream
            pdf_reader = PyPDF2.PdfReader(pdf_bytes)
            page_count = len(pdf_reader.pages)
            max_pages = min(page_count, 50)

            text_parts = []
            for page_num in range(max_pages):
                page = pdf_reader.pages[page_num]
                # PyPDF2's extract_text can return None in some cases
                page_text = page.extract_text() or ""
                text_parts.append(page_text)

            extracted_text = "\n\n".join(text_parts)

        # Step 3: Clean and limit the text
        extracted_text = " ".join(extracted_text.split())

        if len(extracted_text) > 100000:
            extracted_text = extracted_text[:100000] + "\n\n[Text truncated due to length...]"

        # Check if we actually got meaningful text
        if len(extracted_text.strip()) < 100:
            return {
                "status": "error",
                "text": None,
                "page_count": page_count,
                "message": "PDF text extraction yielded very little text. PDF may be scanned/image-based."
            }

        return {
            "status": "success",
            "text": extracted_text,
            "page_count": page_count,
            "message": f"Successfully extracted text from {max_pages} pages"
        }

    except requests.exceptions.Timeout:
        return {
            "status": "error",
            "text": None,
            "page_count": None,
            "message": "Request timed out. The PDF source may be slow or unavailable."
        }

    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "text": None,
            "page_count": None,
            "message": f"Failed to download PDF: {str(e)}"
        }

    except Exception as e:
        return {
            "status": "error",
            "text": None,
            "page_count": None,
            "message": f"Unexpected error processing PDF: {str(e)}"
        }


# Test function for development
if __name__ == "__main__":
    # Quick smoke test with a known arXiv PDF
    print("Testing PDF fetcher for ResearchForge AI with a known paper...")
    result = fetch_pdf("https://arxiv.org/pdf/1706.03762.pdf")

    print(f"Status: {result['status']}")
    print(f"Page Count: {result['page_count']}")
    print(f"Message: {result['message']}")
    if result['status'] == 'success':
        print(f"Text Preview (first 300 chars):\n{result['text'][:300]}...")
