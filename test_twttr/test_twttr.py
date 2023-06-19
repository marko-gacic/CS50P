from twttr import shorten

def main():
    test_shorten()
    test_capitalized()
    test_number()
    test_punctuation()

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("marko") == "mrk"

def test_capitalized():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("MARKO") == "MRK"

def test_number():
    assert shorten("tw1tter") == "tw1ttr"
    assert shorten("mark0") == "mrk0"

def test_punctuation():
    assert shorten("tw,itter") == "tw,ttr"

if __name__ == "__main__":
    main()