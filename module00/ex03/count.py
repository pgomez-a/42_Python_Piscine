import sys

def text_analyzer(user_input=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text. """
    if user_input is None:
        user_input = input("What is the text to analyze?\n>> ")
    if type(user_input) is not str:
        print("AssertionError: argument is not a string")
    else:
        upper = 0
        lower = 0
        space = 0
        punct = 0
        for elem in user_input:
            if elem.islower():
                lower += 1
            elif elem.isupper():
                upper += 1
            elif elem in ('.', ',', ';', '\'', '\"', '-', '!', '?'):
                punct += 1
            elif elem.isspace():
                space += 1
        print("The text contains", len(user_input), "character(s):")
        print("-", upper, "upper letter(s)")
        print("-", lower, "lower letter(s)")
        print("-", punct, "punctuation mark(s)")
        print("-", space, "space(s)")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()
