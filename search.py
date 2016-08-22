#program to read through and count number of contacts in phonebook

phonebook = open("contacts.txt", "r")
numentries = 0
list = []

firstname = phonebook.readline().rstrip()

list.append(firstname)

while firstname != "":
    streetname = phonebook.readline().rstrip()
    town = phonebook.readline().rstrip()
    city = phonebook.readline().rstrip()
    postcode = phonebook.readline().rstrip()
    phonenum = phonebook.readline().rstrip()

    numentries = numentries + 1

    firstname = phonebook.readline().rstrip()
    list.append(firstname)

print "You have", numentries, " entries in your phone book."

print list
