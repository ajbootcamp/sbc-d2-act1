text = "summer bootcamp"

print(text.title())
print(text.capitalize().replace("p", "P"))
print("{0}{1}" .format (text[11:14], text[4].upper()))
print(text[7:11].replace("b", "L"))
print("{1}{0}" .format(text[5], text[12]).upper())
print(text.replace(" ", "").isalpha())