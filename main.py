def main():
    get_word_count(get_book_text("books/frankenstein.txt"))

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    word_list = []
    word_list = text.split()
    num_words = len(word_list)
    print(f"{num_words} words found in the document")


main()
