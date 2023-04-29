def bubble_sort(str):
    n = len(str)
    for i in range(n):
        for j in range(0, n-i-1):
            if str[j] > str[j+1]:
                str = str[:j] + str[j+1] + str[j] + str[j+2:]
    return str


def is_anagram(first_string, second_string):
    sorted_first_string = bubble_sort(first_string.lower())
    sorted_second_string = bubble_sort(second_string.lower())

    if first_string == "" or second_string == "":
        return (sorted_first_string, sorted_second_string, False)

    result_is_anagram = sorted_first_string == sorted_second_string
    return (sorted_first_string, sorted_second_string, result_is_anagram)
