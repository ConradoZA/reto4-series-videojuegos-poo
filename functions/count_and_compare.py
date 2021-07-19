def count_and_list(count_list: list)->list:
    rented_list = []

    for item in count_list:
        if item.estaPrestado(): rented_list.append(item)

    return rented_list


def make_compare(array: list) -> object:
    longest: object = None
    for item in array:
        i = 0
        while i < len(array):
            compare = item.compararCon(array[i])
            if compare == "Mayor":
                longest = item
            elif compare == "Menor":
                longest = array[i]
            i += 1
    return longest
