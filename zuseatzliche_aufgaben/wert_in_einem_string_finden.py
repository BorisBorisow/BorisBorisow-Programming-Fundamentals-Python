formatiert = "{:d}"
print(formatiert.format(7000))
formatiert = "{:,d}"
print(formatiert.format(7000))
formatiert = "{:^15,d}"
print(formatiert.format(7000))
formatiert = "{:*^15,d}"
print(formatiert.format(7000))
formatiert = "{:*^15.2f}"
print(formatiert.format(7000))
formatiert = "{:*>15X}"
print(formatiert.format(7000))
formatiert = "{:*<#15x}"
print(formatiert.format(7000))
formatiert = "Ein {0} {1} und ein {0} {2}."
print (formatiert.format("blaues", "Auto", "Boot"))