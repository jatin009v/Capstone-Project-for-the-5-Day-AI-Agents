"""
Citation extraction and formatting tools for ResearchForge AI

These utilities are used by the PaperAnalyzerAgent to produce clean,
validated APA-style citations and BibTeX entries. The logic is designed
to remain lightweight but reliable within the ResearchForge multi-agent
pipeline.
"""

from typing import List, Dict
from datetime import datetime


def extract_citation(
    title: str,
    authors: List[str],
    year: int,
    venue: str = ""
) -> Dict:
    """
    Generates a structured citation (APA style) and BibTeX entry
    using validated metadata.

    Used inside ResearchForge's paper analysis stage.
    """
    try:
        # Validate metadata first
        validated = validate_citation_metadata(title, authors, year, venue)

        title = validated["validated_title"]
        authors = validated["validated_authors"]
        year = validated["validated_year"]
        venue = validated["validated_venue"]

        if validated["validation_issues"]:
            print(f"[ResearchForge] Citation validation issues: {validated['validation_issues']}")

        # Format author names into APA format
        formatted_authors = format_authors_apa(authors)

        # Build final citation
        citation_parts = [
            formatted_authors,
            f"({year})",
            f"*{title}*"
        ]

        if venue and venue != "Unknown Venue":
            citation_parts.append(f"*{venue}*")

        citation = ". ".join(citation_parts) + "."

        # Generate BibTeX
        bibtex = generate_bibtex(title, authors, year, venue)

        return {
            "status": "success",
            "citation": citation,
            "bibtex": bibtex,
            "validation_issues": validated["validation_issues"],
            "message": "Citation generated successfully (ResearchForge)"
        }

    except Exception as e:
        return {
            "status": "error",
            "citation": None,
            "bibtex": None,
            "message": f"ResearchForge citation error: {str(e)}"
        }


def format_authors_apa(authors: List[str]) -> str:
    """
    Formats a list of authors into APA citation style.

    Example:
        ["Ashish Vaswani", "Noam Shazeer"] =>
        "Vaswani, A. & Shazeer, N."
    """

    def format_single_author(name: str) -> str:
        """Convert 'First Last' to 'Last, F.' with robust parsing."""
        if not name or name.strip() == "":
            return "Unknown"

        if "et al" in name.lower():
            return "et al."

        parts = name.strip().split()

        # Single name: keep it simple
        if len(parts) == 1:
            return f"{parts[0]}."

        # Standard format
        last_name = parts[-1]
        first_initial = parts[0][0].upper() + "."

        return f"{last_name}, {first_initial}"

    if not authors:
        return "Unknown"

    valid = [a for a in authors if a and a.strip()]
    if not valid:
        return "Unknown"

    formatted = [format_single_author(a) for a in valid]

    # APA list formatting
    if len(formatted) == 1:
        return formatted[0]
    if len(formatted) == 2:
        return f"{formatted[0]} & {formatted[1]}"

    return f"{', '.join(formatted[:-1])}, & {formatted[-1]}"


def generate_bibtex(title: str, authors: List[str], year: int, venue: str) -> str:
    """
    Generates a BibTeX entry for the paper.
    """

    first_author = authors[0].split()[-1].lower() if authors else "unknown"
    cite_key = f"{first_author}{year}"

    bibtex_authors = " and ".join(authors)

    bibtex = f"""@article{{{cite_key},
  title={{{title}}},
  author={{{bibtex_authors}}},
  year={{{year}}},
  venue={{{venue}}}
}}"""

    return bibtex


def validate_citation_metadata(title: str, authors: List[str], year: int, venue: str) -> Dict:
    """
    Validates and corrects citation metadata before formatting.
    """

    issues = []

    # Title
    if not title or len(title.strip()) < 5:
        issues.append("Title too short or missing")
        title = "Unknown Title"

    # Authors
    if not authors:
        issues.append("No authors provided")
        authors = ["Unknown"]
    else:
        authors = [a.strip() for a in authors if a and a.strip()]
        if not authors:
            authors = ["Unknown"]

    # Year
    if not year or year < 1900 or year > 2030:
        issues.append(f"Invalid year: {year}")
        year = datetime.now().year

    # Venue
    if not venue or len(venue.strip()) < 2:
        issues.append("Venue missing or too short")
        venue = "Unknown Venue"

    return {
        "validated_title": title,
        "validated_authors": authors,
        "validated_year": year,
        "validated_venue": venue,
        "validation_issues": issues
    }


# Development test
if __name__ == "__main__":
    print("Testing ResearchForge citation formatter...")

    result = extract_citation(
        title="Attention Is All You Need",
        authors=["Ashish Vaswani", "Noam Shazeer"],
        year=2017,
        venue="NeurIPS"
    )
    print("\nTest 1:")
    print(result["citation"])
    print(result["bibtex"])
