import re

# name = "Darpan"
#
# srting = "Hello Guys This Is Darpan Salunke !... How are You Darpan "
#
# if re.search(name, srting):
#     print("Match")
# else:
#     print("Not Match")

# split_sign = '@'
#
# str_ing = 'darpansalunke@gmail.com'
#
# print(re.split(split_sign,str_ing))

name = "Darpan"

srting = "Hello Guys This Is Darpan Salunke !... How are You Darpan "

print(re.findall(name, srting))
