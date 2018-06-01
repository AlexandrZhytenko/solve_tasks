# You are given a string with words and numbers
# separated by whitespaces (one space).
# You should check if the string contains three words in succession.

def find_words(input_string):
    count = 0
    inp_str = input_string.lower()
    for i in str.rsplit(inp_str):
        if i.isalpha():
            count += 1
            if count >= 3:
                return True
        else:
            count = 0
    return False

if __name__ == "__main__":
    print find_words("one two 3 four five six 7 eight 9 ten eleven 12")
    print find_words("Hello World hello")
    print find_words("He is 123 man")
    print find_words("1 2 3 4")