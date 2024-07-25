string = "Hello World"
string1 = ""
index = 0
for letter in string:
    index += 1
    if index % 2 == 0:
        string1 += letter
    else:
        string1 += letter.upper()
print(string1)

str = "Hello World!"
rev_str = str[::-1]
print(rev_str)

string2 = "I am learning to code"
string3 = ""
split_string2 = string2.split()
index = 0
for word in split_string2:
    index += 1
    if index % 2 == 0:
        string3 += word + " "
    else:
        string3 += word.upper() + " "
print(string3)