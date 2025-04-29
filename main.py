import sys
from stats import get_num_words, get_num_char, sort_dictionary

# MAIN FUNCTION
def main():
    sys.argv
    book = ""
    word_count = []

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")

    print("----------- Word Count ----------")
    get_num_words(get_book_text(book))

    print("--------- Character Count -------")
    word_count = sort_dictionary(get_num_char(get_book_text(book)))
    for word in word_count:
        print(f"{word["char"]}: {word["num"]}")

    print("============= END ===============")

# FIND BOOK AND RETURN CONTENTS AS A STRING
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# CALL MAIN
main()