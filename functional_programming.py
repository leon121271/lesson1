def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        results[func.__name__] = func(int_list)
    return results

print(apply_all_func([6.1, 20.4, 15.87, 9], max, min))
print(apply_all_func([1.15, 12.05, 15, 9.9], len, sum, sorted))