
def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_letters(book_text):
    char_counts = {}
    text = book_text.lower()

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

