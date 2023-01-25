first_string = input().split(", ")
second_string = input().split(", ")
replaced_words = [word for word in first_string if\
                  any(word in second_word for second_word in second_string)]
print(replaced_words)

# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# my_list.sort(reverse=True)
# my.list.pop()
# my_list.insert(i, elem)
# number = my_list.index(2)
# repetition = my_list.count(2)
# my_list.reverse()
# del my_list[x]
# my_list.remove(1)
# print(my_list)

# matrix = [[1,2,3,4,5], [6,7,8,9,10]]
#
# print(matrix[0][3])
