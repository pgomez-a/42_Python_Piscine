import sys

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    user_input = int(sys.argv[1])
    if (user_input == 0):
        print("I'm Zero.")
    elif (user_input % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
elif len(sys.argv) == 2:
    print("AssertionError: argument is not an integer")
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
