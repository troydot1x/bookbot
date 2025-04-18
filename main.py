
from stats import get_num_words, get_num_letters

filepath = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    the_book = get_book_text(filepath)
    print(the_book)


book_text = get_book_text(filepath)
word_count = get_num_words(book_text)
letter_count = get_num_letters(book_text)
print(f"{word_count} words found in the document")
print(letter_count)

#main()