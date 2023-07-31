def key_value_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result


print(key_value_dict(а=1, б=2, в=3, г=4, д=5))