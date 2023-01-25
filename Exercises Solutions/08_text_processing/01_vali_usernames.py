import string


def valid_username(data):
    expected_elements = string.digits + string.ascii_letters + "_" + "-"
    for user in data:
        if len(user) >= 3 and len(user) <= 16 and len([x for x in user if x in expected_elements]) == len(user):
            print(user)
        else:
            continue


d = input().split(", ")
valid_username(d)

# import string
#
#
# def valid_usernames(data):
#     flag = 0
#     expected_elements = string.digits + string.ascii_letters + "_" + "-"
#     for user in data:
#         if len(user) < 3 or len(user) > 16:
#             continue
#         elif len([x for x in user if x in expected_elements]) != len(user):
#             continue
#         else:
#             print(user)
#
#
# d = input().split(", ")
# valid_usernames(d)
