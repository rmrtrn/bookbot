from stats import get_num_words
from stats import get_chars_dict
from stats import chars_dict_to_sorted_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        text = f.read()
        return text
    
def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_dicts_list = chars_dict_to_sorted_list(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")
    print("--------- Character Count -------")
    for item_dict in sorted_dicts_list:
        if item_dict["char"].isalpha():
            print(f"{item_dict['char']}: {item_dict['num']}")
    print("============= END ===============")


main()