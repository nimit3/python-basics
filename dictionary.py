
# student = {
#     "name": "nimit",
#     "age": 26,
#     "isLegal": True
# }

# student['isPR'] = True
# print(student)
# print(student)
# # how to print some specific value
# # ----------------get() method--------------
# print(student["age"])
# print(student.get("namee"))  # will print none instead of giving error
# print(student.get("isMarried", "false"))  # we can put default value too
# print(student.get('xxx')) # will print None because it's not avlble

# # looping thorugh object method 1
# for i in student:
#     print (student[i])
# # looping thorugh object method 2
# for value in student.values():
#     print(value)
# # looping thorugh object's key
# for key in student.keys():
#     print(key)

# accessing key and value both at a same time ------ using items()
# print(student.items())
# for key,value in student.items():
#     print(f'key is {key} & value is {value}')

# print(student["age"])
# JS key, index style iterating
# days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
# # with enurmate we can print the index value too. like normal function in JS
# for i, day in enumerate(days):
#     print(f'index no is {i} and day is {day}')

# # we can use in function like string and list here too
# print("name" in student)
# print("name" in student.keys())
# print(26 in student.values())

# -------------------------------DICTIONARY METHODS-------------------------------------
#  1) clear() - will clear out everyhting

#  2) copy() - will save copy/clone of the same dictionary

# student = {
#     "name": "nimit",
#     "age": 26,
#     "isLegal": True,
#     "catName": "biladi"
# }

# # pop(element) - for removing some spicific key value pair
# student.pop("age") #student.pop() won't work. at least need one args(key)
# print(student)

# for removing any item
# student.popitem() # will remove last item
# print(student)

#  update() --- will take all key, value pair of 1 dictionary into another 1
# ss = dict(city='toronto', ffe='gg')
# ss.update(student)
# print(ss) # will have all student obj key value pair

# -------------------NESTED LIST AND DICTIONARY----------------
playlist = {
    'title': 'patagonia bus',
    'author': 'colt steele',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
        {'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
        {'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
    ]
}

print(playlist['songs'][2]['title'])  # will print meowmeow

totalTime = 0
for song in playlist['songs']:
    totalTime = totalTime + song['duration']
print(totalTime)
