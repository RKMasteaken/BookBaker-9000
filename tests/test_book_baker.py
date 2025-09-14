import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import book_baker


def test_generate_book_word_count():
    cfg = book_baker.BookConfig(idea="history", pages=2)
    content = book_baker.generate_book(cfg)
    assert len(content.split()) >= 2 * book_baker.WORDS_PER_PAGE


def test_rating_tips_star():
    tips = book_baker.rating_tips("stars")
    assert any("narrative" in tip for tip in tips)
