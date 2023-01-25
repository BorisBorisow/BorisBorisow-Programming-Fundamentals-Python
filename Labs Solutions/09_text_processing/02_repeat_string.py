some_string = input().split(" ")
repeated_string = ""
for ch in some_string:
    repeated_string += ch * len(ch)

print(repeated_string)
