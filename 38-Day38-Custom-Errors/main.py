# a = input("Enter any value between 5 and 9: ")

# if(a.lower() == "quit"):
#     print("Program Ended!")
# else:
#     a = int(a)
#     if(a < 5 or a > 9):
#         raise ValueError("Value should be between 5 and 9")


class CustomError(Exception):
    pass


try:
    a = input("Enter any value between 5 and 9: ")

    if a.lower() == "quit":
        print("Program Ended!")

    else:
        a = int(a)

        if a < 5 or a > 9:
            raise CustomError("Value should be between 5 and 9!")

except CustomError:
    print("Value should be between 5 and 9")
