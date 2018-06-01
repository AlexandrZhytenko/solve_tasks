# Find Nth power of the element with index N.
import math

def index_power(input_list=[], index=0):
    try:
        return math.pow(input_list[index], index)
    except IndexError:
        return -1

# # or
# def index_power(input_list=[], index=0):
#     return input_list[index] ** index if index < len(input_list) else -1


if __name__ == "__main__":
    input_list = [1, 2, 3, 4]
    index = 2
    print index_power(input_list, index)