###### testing python functions 
# names = ['prince', 'princess', 'king']
# def add_name(name):
#     names.append(name)
#     print(names)
#     for x in names:
#         print(x)

# add_name('queen')


###### Reading a text files
# f = open("C:\\Users\\USER\\Desktop\\context.txt", "r")
# print(f.read())
# f.close()

#### appending or writing into a txt file
# f = open("C:\\Users\\USER\\Desktop\\context.txt", "a")
# f.write("Hello, a new line")
# f.close()
###### Reading from a docx 
# from docx import Document

# doc = Document("C:\\Users\\USER\\Desktop\\Resume.docx")

# # Read and print the text content
# for p in doc.paragraphs:
#     print(p.text)


###### creating a new file and writing into it
# f = open("new.txt", "w")
# f.write("Hello this is a new file \n I was just practising my python")


#### removing a file
import os

if os.path.exists("new.txt"):
    os.remove("new.txt")
else:
    print("file does not exist")



