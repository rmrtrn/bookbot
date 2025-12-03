def get_num_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def get_chars_dict(text):
    chars_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_dicts_list = []
    for char, num in chars_dict.items():
        new_dict = {"char": char, "num" : num}
        sorted_dicts_list.append(new_dict)
    
    sorted_dicts_list.sort(reverse=True, key=sort_on)
    return sorted_dicts_list
    

