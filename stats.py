def get_num_of_words(text):
    words = text.split()
    return len(words)

def get_num_of_each_char(text):
    char_count = {}
    for char in text:
        lower = char.lower()
        if lower in char_count:
            char_count[lower] += 1
        else:
            char_count[lower] = 1
    return char_count


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
