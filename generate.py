# import string
# for w in string.ascii_lowercase:
#     for x in string.ascii_lowercase:
#         for y in string.ascii_lowercase:
#             for z in string.ascii_lowercase:
#                 print w+x+y+z

def generateCase():
    x = open("jCustom.txt")
    d = x.readlines()
    results = []
    for line in d:
        results.append(line.upper())
    results = d+results
    x = open("jCustomUpper.txt", "w")
    x.writelines(results)
    x.close()
generateCase()
