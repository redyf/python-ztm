# Error Handling
# Example 1
while True:
    try:
        age = int(input("What is your age?"))
        # raise ValueError("Hey cut it out")
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter an age higher than 0")
    else:
        print("Thank you")
        break
    finally:
        print("Ok, I'm finally done")
    print("Can you hear me?")


# Example 2
# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(f"Please enter numbers, {err}")
#
#
# print(sum(1, "2"))
