# find the max value from dictionary

def max_value_from_dictionary(input_dict):
    """
        >>> max_value_from_dictionary({'a': 1, 'b': 2, 'c': 3})
        'c'
        >>> max_value_from_dictionary({'a': 3, 'b': 2, 'c': 1})
        'a'
        """
    return sorted(input_dict.items(), key=lambda x: x[1], reverse=True)[0][0]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
