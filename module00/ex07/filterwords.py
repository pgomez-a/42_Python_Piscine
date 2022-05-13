import sys

if len(sys.argv) != 3:
    print("ERROR")
    exit(1)

input_str = sys.argv[1]
input_len = sys.argv[2]
if not input_len.isdigit():
    print("ERROR")
    exit(1)

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
input_len = int(input_len)
input_list = input_str.split()
output_list = list()
for word in input_list:
    word = [letter for letter in word if letter not in punc]
    output_list.append(''.join(word))
output_list = [item for item in output_list if len(item) > input_len]
print(output_list)
