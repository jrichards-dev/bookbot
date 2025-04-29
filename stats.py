def get_num_words(text):
    word_list = []
    word_list = text.split()
    num_words = len(word_list)
    print(f"{num_words} words found in the document")