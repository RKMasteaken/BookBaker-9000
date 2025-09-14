from dataclasses import dataclass
from typing import List

WORDS_PER_PAGE = 300

@dataclass
class BookConfig:
    idea: str
    pages: int
    rating_system: str = "stars"  # 'stars' or 'content'


def generate_book(config: BookConfig) -> str:
    """Generate placeholder content for a non-fiction book.

    The function expands the idea into enough words to roughly match the
    requested number of pages. Each page is approximated as 300 words.
    """
    base_sentence = f"This section explores {config.idea} in depth. "
    words_needed = config.pages * WORDS_PER_PAGE
    reps = (words_needed // len(base_sentence.split())) + 1
    content = (base_sentence * reps).strip()
    return content


def rating_tips(system: str) -> List[str]:
    """Return tips to help increase a book's rating."""
    if system == "stars":
        return [
            "Organize chapters with a clear narrative arc",
            "Use engaging and well-researched anecdotes",
            "Edit thoroughly for grammar and clarity",
        ]
    else:
        return [
            "Avoid gratuitous violence or explicit language",
            "Provide content warnings where appropriate",
            "Highlight educational or positive themes",
        ]


def format_for_publishing(config: BookConfig, content: str) -> str:
    """Format the book and tips as Markdown for easy publishing."""
    tips = rating_tips(config.rating_system)
    header = f"# {config.idea}\n\n"
    header += "## Tips to Increase Rating\n"
    for tip in tips:
        header += f"- {tip}\n"
    header += "\n## Content\n\n"

    # Split content into page-sized chunks
    words = content.split()
    pages = []
    for i in range(config.pages):
        start = i * WORDS_PER_PAGE
        end = (i + 1) * WORDS_PER_PAGE
        page_words = words[start:end]
        pages.append(" ".join(page_words))

    for i, page in enumerate(pages, 1):
        header += f"### Page {i}\n{page}\n\n"
    return header


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="BookBaker-9000")
    parser.add_argument("idea", help="Central idea for the book")
    parser.add_argument("pages", type=int, help="Number of pages desired")
    parser.add_argument("--rating", default="stars", choices=["stars", "content"],
                        help="Rating system to optimize for")
    args = parser.parse_args()

    cfg = BookConfig(idea=args.idea, pages=args.pages, rating_system=args.rating)
    content = generate_book(cfg)
    formatted = format_for_publishing(cfg, content)
    print(formatted)
