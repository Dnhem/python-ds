def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    lst = [1, 2, 3, 4, 5]
    odd = []
    for i, v in enumerate(lst):
        if (i % 2 == 0):
            odd.append(lst[i])
    return odd

    #List Comprehension    
    # return [v for i, v in enumerate(lst) if i % 2 == 0]

