def func_sum(first_word, second_word):
    result = 0
    for i in range(len(first_word)):
        if i < len(second_word):
            result += ord(first_word[i]) * ord(second_word[i])
        else:
            result += ord(first_word[i])

    return result


def char_multiplier(first_word, second_word):
    result = 0
    if len(first_word) > len(second_word):
        result = func_sum(first_word, second_word)
    else:
        result = func_sum(second_word, first_word)

    print(result)


data = input().split(" ")

char_multiplier(data[0], data[1])
