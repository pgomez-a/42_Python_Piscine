import sys

if len(sys.argv) <= 2:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")
elif len(sys.argv) != 3:
    print("AssertionError: too many arguments")
elif sys.argv[1].isdigit() and sys.argv[2].isdigit():
    numberOne = int(sys.argv[1])
    numberTwo = int(sys.argv[2])
    print("Sum:       ", numberOne + numberTwo)
    print("Difference:", numberOne - numberTwo)
    print("Product:   ", numberOne * numberTwo)
    if numberTwo != 0:
        print("Quotient:  ", numberOne / numberTwo)
        print("Remainder: ", numberOne % numberTwo)
    else:
        print("Quotient:   ERROR (division by zero)")
        print("Remainder:  ERROR (modulo by zero)")
else:
    print("AssertionError: only integers")
