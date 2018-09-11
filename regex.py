import re

list = str(["Leeds", "Harrogate", "Garforth", "Leeds", "1234", "5678", "1321"])
number_list = str([4000, 1321, 1, 1000, 100, 30, 4050])
other = []

#regex = other.append(re.findall("Leeds", list))
regex = re.findall("Leeds", list)

print(regex)

#numbers = re.search("[1-4][0-9][0-9][0-9]", number_list)

numbers = re.search("[1-4]?[0-9]{1,3}", number_list).group(0)
numbers2 = re.findall("[1-4]?[0-9]{1,3}", number_list)
#numbers3 = re.findall("^[1-9]$", number_list)

print(numbers)
print(numbers2)
#print(numbers3)

def get_vlan(text):
    vlan = re.search("[1-4]?[0-9]{1,3}", text).group(0)
    return vlan

print(get_vlan(number_list))

'''
def get_interfaces(text):
    interfaces = re.findall("[1-4]?[0-9]{1,3}", text)
    return interfaces
'''
