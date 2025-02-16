


def main():
    path_to_file = "books/frankenstein.txt"
    file_text = get_book_text(path_to_file)
    letter_dictionary = count_characters(file_text)
    word_count = count_words(file_text)
    listed_dict = list_it(letter_dictionary)
    sorted_d = sort_dict(listed_dict)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in document")
    
    report_alphabet(sorted_d)
    
    print("--- End report ---")
    
    #print(f"word count:  {word_count}")
    
    #print(letter_dictionary)
    
    #print(report)
    


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

def list_it(dict):
    return [{key: value} for key, value in dict.items()]    

def sort_dict(list_dict):
    sorted_dictionary = []
    for pair in list_dict:
        key = next(iter(pair))
        if key.isalpha():
            sorted_dictionary.append(pair)
    #sorted_dictionary.sort(key=str.isalpha(), reverse=False)       
    return sorted_dictionary

def report_alphabet(sorted_dict):
    for letter in sorted_dict:
        key = next(iter(letter))
        print(f"The '{key}' character was found {letter[key]} times")
    return
    
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