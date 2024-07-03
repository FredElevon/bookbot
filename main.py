def get_file_content(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_wordcount(str):
    return len(str.split())


def get_letter_count(str):
    str = str.lower()

    letters_set = set()
    for i in set(str):
        if i.isalpha():
            letters_set.add(i)

    letter_dict = {}
    for letter in letters_set:
        letter_dict[letter] = str.count(letter)

    return letter_dict


def dict_to_sorted_list(dict):
    sorted_list = []
    for key in dict:
        sorted_list.append({"letter": key, "count": dict[key]})
    sorted_list.sort(reverse=True, key=lambda d: d["count"])
    return sorted_list


def print_freq_of_letters(sorted_list):
    for item in sorted_list:
        print(f"Letter {item['letter']} was found {item['count']} times")


def print_histo(sorted_list):
    sum_letters = 0
    for item in sorted_list:
        sum_letters += item["count"]

    for item in sorted_list:
        relative_count = (item["count"] * 100) // sum_letters
        bar = "=" * relative_count * 5
        if relative_count > 0:
            print(f"{ item['letter'] } { bar }")


def main():
    book_path = "books/frankenstein.txt"
    book_str = get_file_content(book_path)
    word_count = get_wordcount(book_str)
    letter_dict = get_letter_count(book_str)
    sorted_list = dict_to_sorted_list(letter_dict)

    print(f"The book {book_path} contains {word_count} words.\n")
    print_freq_of_letters(sorted_list)
    print_histo(sorted_list)


main()
