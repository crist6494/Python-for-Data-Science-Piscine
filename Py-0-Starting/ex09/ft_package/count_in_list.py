def count_in_list(lst, item):
    """
    Count the number of times item appears in lst.
    """

    if lst is None or item is None:
        raise Exception("Wrong arguments")
    return lst.count(item)
