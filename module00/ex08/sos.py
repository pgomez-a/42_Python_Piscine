import sys

if len(sys.argv) == 1:
    exit(1)

MORSE_CODE_DICT = { ' ':'/', 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

input_str = ' '.join(sys.argv[1:])
input_str = input_str.split()
input_str = ' '.join(input_str)
input_str = input_str.upper()
for item in input_str:
    if not item.isalnum() and not item.isspace():
        print("ERROR")
        exit(1)

for item in input_str:
    print(MORSE_CODE_DICT[item], end=" ")
print()
