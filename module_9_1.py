
def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)

    return results


def min_list(list_):
    return min_list(list_)


def max_list(list_):
    return max_list(list_)


def len_list(list_):
    return len_list(list_)


def sum_list(list_):
    total = 0
    for x in list_:
        total += x
    return total


def sorted_list(list_):
    return sorted(list_)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))