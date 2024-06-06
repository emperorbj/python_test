# testing python functions 
names = ['prince', 'princess', 'king']
def add_name(name):
    names.append(name)
    print(names)
    for x in names:
        print(x)

add_name('queen')