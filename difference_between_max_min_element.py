# find the difference between the maximum and minimum element

def difference_between_max_min_element(*args):
    if list(args):
        return max(list(args)) - min(list(args))
    return "Empty input arguments"

if __name__ == "__main__":
    print difference_between_max_min_element(1,2,3)