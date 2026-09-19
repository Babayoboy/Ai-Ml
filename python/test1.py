info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]
# All THE UNIQUE COURCE
# unique_cource = set()
# for tupe in info:
#     unique_cource.add(tupe[1])
# print(list(unique_cource))

# ALL THE STUDENTS ENROLLED IN ENGLISH
# student_engish = []
# for tupe in info:
#     if(tupe[1] == "English"):
#         student_engish.append(tupe[0])
# print(student_engish)

# Dictornary
info_dic = {}
for name,cource in info:
    if info_dic.get(name) == None:
        info_dic.update({name: {cource}})
    else:
        info_dic[name].add(cource)
print(info_dic)
