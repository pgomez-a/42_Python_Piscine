import sys

user_input = str()

for pos in range(len(sys.argv)):
    if pos != 0:
        user_input += sys.argv[pos]
        if pos + 1 < len(sys.argv):
            user_input += ' '

user_output = user_input[::-1]
print(user_output.swapcase())
