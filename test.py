# testing python functions 
# names = ['prince', 'princess', 'king']
# def add_name(name):
#     names.append(name)
#     print(names)
#     for x in names:
#         print(x)

# add_name('queen')

f = open("test.txt", "r")
print(f.read())

for x in f:
    print(x)
    
f.close()