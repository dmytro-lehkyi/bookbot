def words_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count

def print_report(file_path):
    print(f"--- Begin report of {file_path} ---")

    with open(file_path) as f:
        text = f.read()
        print(f"{words_count(text)} words found in the document")

        for char, count in char_count(text).items():
            if char.isalpha():
                print(f"The '{char}' character was found {count} times")

        print("--- End report ---")
    # print(char_count(text))

file_path = "books/frankenstein.txt"
print_report(file_path)
