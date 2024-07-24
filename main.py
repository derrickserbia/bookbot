def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words_in_text(text)
    characters = count_characters_in_text(text)
    print_character_dictionary_report(book_path, word_count, characters)

def sort_on(dict):
    return dict["count"]

def print_character_dictionary_report(book_path, word_count, character_dictionary):

    character_list = dict_to_list(character_dictionary)
    character_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in document")
    for item in character_list:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found '{item['count']}' times")
    print("--- End report ---")


def dict_to_list(dict):
    returnList = []
    for k in dict:
        returnList.append({"char": k, "count": dict[k]})

    return returnList

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words_in_text(text):
    words = text.split()
    return len(words)

def count_characters_in_text(text):
    character_count = {}
    lowered_string = text.lower()

    for c in lowered_string:
        if not (c in character_count):
            character_count[c] = 1
        else:
            character_count[c] += 1

    return character_count

main()