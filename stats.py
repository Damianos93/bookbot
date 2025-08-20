def get_word_count(text):
    splitted_text = text.split()
    number_of_words = len(splitted_text)
    return number_of_words


def get_char_count(text):
    result = {}

    for char in text:
        lowered_char = char.lower()
        if lowered_char in result:
            result[lowered_char] += 1
        else:
            result[lowered_char] = 1
    return result


def sort_on(items):
    return items["num"]


def make_list_of_dict(dict):
    result = []
    for char in dict:
        if char.isalpha():
            num = dict[char]
            new_dict = {}
            new_dict["char"] = char
            new_dict["num"] = num
            result.append(new_dict)
    result.sort(reverse=True, key=sort_on)
    return result
