import random

def generator(text, sep=" ", option = None):
    """Splits the text according to sep value and yield the substrings.
       option precise if a action is performed to the substring before it is yielded."""
    if not type(text) == str or not type(sep) == str or (option != None and not type(option) == str):
        print("ERROR")
        return
    if option != None and option not in ["shuffle", "unique", "ordered"]:
        print("ERROR")
        return
    gen_list = text.split(sep)
    if option != None and option == "shuffle":
        random.shuffle(gen_list)
    elif option != None and option == "unique":
        gen_list = set(gen_list)
    elif option != None and option == "ordered":
        gen_list.sort()
    for item in gen_list:
        yield item
    return
