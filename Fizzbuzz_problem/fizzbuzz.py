from tkinter.tix import InputOnly


def fizzbuzz(Input):
    if (Input % 3 == 0 & Input % 5 == 0):
        return "fizbuzz"
    elif (Input % 5 == 0):
        return "buzz"
    elif (Input % 3 == 0):
        return "fizz"
    else:
        return Input


print(fizzbuzz(5))
