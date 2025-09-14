# BookBaker-9000

BookBaker-9000 is a simple command-line tool that turns an idea into a
customizable non-fiction book.

## Usage

```
python book_baker.py "The History of Tea" 3 --rating content > tea_book.md
```

The first argument is the central idea for the book. The second argument
specifies the number of pages to generate. The optional `--rating` flag
chooses the rating system to optimise for (`stars` or `content`).

The script outputs Markdown that includes:

- Automatically generated book content.
- Tips for improving the book's rating.
- Page-by-page sections ready for publishing.

## Development

Run tests with:

```
pytest
```
