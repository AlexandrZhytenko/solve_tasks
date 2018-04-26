# find the sum of the elements with even indexes (0th, 2nd, 4th...)
# then multiply this summed number and the
# final element of the array togethe

def sum_items(array):
    if array:
        return sum([array[i] for i in range(len(array)) if i % 2 == 0])*array[-1]
    return 0

if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5]
    print sum_items(array)