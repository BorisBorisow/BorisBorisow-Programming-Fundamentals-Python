class Party:
    def __init__(self):
        self.people = []


party = Party()

going = input()
while going != "End":
    party.people.append(going)
    going = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")


# class Party:
#     def __init__(self):
#         self.going = "Going: "
#         self.total_count = 0
#     def go(self, name):
#         self.going += name
#         self.going += ", "
#         self.total_count += 1
#
#
# party = Party
#
# while True:
#     name = input()
#     if name == "End":
#         break
#     party.go(name)
#
# print(party.going[:-2])
# print(party.total_count)

# party
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Party:
#     def __init__(self):
#         self.people = []
#
#     def invite(self, person):
#         self.people.append(person)
#
#     def name_of_attendees(self):
#         return ', '.join([person.name for person in self.people])
#
#     def number_of_guests(self):
#         return len(self.people)

