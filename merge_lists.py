# Merge Lists

def merge_lists(list1, list2):
    """
        >>> merge_lists([1,2,4], [1,3,4])
        [1, 1, 2, 3, 4, 4]
        >>> merge_lists([4,2,1], [1,3,4])
        [4, 1, 2, 3, 1, 4]
    """
    result = []
    for i, j in zip(list1, list2):
        result.append(i)
        result.append(j)
    return result

import itertools
def merge_lists1(list1, list2):
    """
        >>> merge_lists1([1,2,4], [1,3,4])
        [1, 1, 2, 3, 4, 4]
        >>> merge_lists1([4,2,1], [1,3,4])
        [4, 1, 2, 3, 1, 4]
    """
    result = []
    for i in itertools.izip(list1, list2):
        result.append(i[0])
        result.append(i[1])
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()