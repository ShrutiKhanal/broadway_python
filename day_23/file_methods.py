# with open("info.txt", "w") as fp:
#     fp.write("Hello World\nWelcome to broadway")

with open("info.txt", "r") as fp:
    data = fp.read() #normal read
    print(data)

    fp.seek(0) #seek() method changes the cursor position to the provided index
    data = fp.read(7)
    print(data)

    fp.seek(0)
    data = fp.readline() #euta line print
    print(data)

    fp.seek(0)
    data = fp.readlines() #list bhitra halera dincha
    print(data)

    print(fp.tell())


data = ["Python is a high-level language\n", "Python is an interpreted  language"]
with open("info.txt", "w") as fp:
    fp.writelines(data)