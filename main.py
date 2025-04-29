from stats import get_num_words
from stats import get_num_char
from stats import sort_dictionary

def main():
    book = "books/frankenstein.txt"
    word_count = []

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")

    print("----------- Word Count ----------")
    get_num_words(get_book_text(book))

    print("--------- Character Count -------")
    word_count = sort_dictionary(get_num_char(get_book_text(book)))
    for word in word_count:
        print(f"{word["char"]}: {word["num"]}")
        
    print("============= END ===============")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()
