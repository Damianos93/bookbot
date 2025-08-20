import sys
from stats import get_word_count, get_char_count, make_list_of_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    num_chars = get_char_count(text)
    sorted_char_list = make_list_of_dict(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
