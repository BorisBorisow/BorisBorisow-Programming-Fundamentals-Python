# print(list(map(lambda x: round(float(x)), input().split())))

def round_func(number):
    # x = [round(float(x)) for x in number]
    # return x
    roundet_list = []
    for x in number:
        roundet_list.append(round(float(x)))
    return roundet_list

numbers = input().split(" ")
print(round_func(numbers))