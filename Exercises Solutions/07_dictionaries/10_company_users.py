command = input().split(" -> ")

companies = {}

while not command[0] == "End":
    company = command[0]
    id = command[1]
    if company not in companies.keys():
        companies[company] = [id]
    else:
        if id not in companies[company]:
            companies[company] += [id]
    #     if company in companies.keys():
    #         if id not in companies[company]:
    #             companies[company].append(id)
    #     else:
    #         companies[company] = [id]
    command = input().split(" -> ")

for company, id in companies.items():
    print(f"{company}")
    print("-- " + ('\n-- '.join(id)))

