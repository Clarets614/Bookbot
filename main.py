


def main():
    path_to_file = "books/frankenstein.txt"
    file_text = get_book_text(path_to_file)
    letter_dictionary = count_characters(file_text)
    word_count = count_words(file_text)
    
    print(f"word count:  {word_count}")
    
    print(letter_dictionary)


def get_book_text(path):
    with open(path) as f:
      file_contents = f.read()
    return file_contents

def count_words(contents):
    words = contents.split()
    count = 0
    for w in words:
        count += 1        
    return count
    
def report_alphabet(dict, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in document")
    
    print("--- End report ---")
    pass
    
def count_characters(input_string):
    lower_case = input_string.lower()
    letter_counts = {}
    for char in lower_case:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
            
    return letter_counts


main()