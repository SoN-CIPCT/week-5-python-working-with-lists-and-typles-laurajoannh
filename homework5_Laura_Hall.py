print("List Exercise:")

print()

insulins = ["NPH","Glargine","Degludec","Lispro","Aspart","Glulisine",]
print (insulins)
print("The first two items in the list are:",  ", ".join(map(str, insulins[0:2])))
print("The middle two items in the list are:", ", ".join(map(str, insulins[2:4])))
print(f"The first and last items in the list are: {insulins[0]}, {insulins[5]}")

print()
print("Tuple Exercise:")
print()

thistuple = ("burger", "pizza", "curry", "pad thai", "oreos")
for item in thistuple:
    print(item)
thislist = list(thistuple)

print()

thislist[1] = "fries"
thislist[3] = "chocolate milkshake"
thistuple2 = tuple(thislist)
for item in thistuple2:
    print(item)
