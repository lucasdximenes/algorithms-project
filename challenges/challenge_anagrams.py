def merge(left, right):
    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res += left[i:]
    res += right[j:]

    return res


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def is_anagram(first_string, second_string):
    sorted_first_string = "".join(merge_sort(first_string.lower()))
    sorted_second_string = "".join(merge_sort(second_string.lower()))

    if first_string == "" or second_string == "":
        return (sorted_first_string, sorted_second_string, False)

    result_is_anagram = sorted_first_string == sorted_second_string
    return (sorted_first_string, sorted_second_string, result_is_anagram)
