# function will receive a positive integer and return:
# "Fizz Buzz" if the number is divisible by 3 and by 5
# "Fizz" if the number is divisible by 3
# "Buzz" if the number is divisible by 5
# The number as a string for other cases

def word_game(number):
    result = ["Fizz Buzz", "Fizz", "Buzz"]
    if number % 3 == 0 and number % 5 == 0:
        return result[0]
    elif number % 3 == 0:
        return result[1]
    elif number % 5 == 0:
        return result[2]
    return str(number)

if __name__ == "__main__":
    print word_game(15)
    print word_game(6)
    print word_game(5)
    print word_game(7)