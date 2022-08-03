def Convert(list):
    res_dct = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
    return res_dct


# Driver code
list = ['a', 1, 'b', 2, 'c', 3]
print(Convert(list))
