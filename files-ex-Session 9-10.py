f = open("x-files.txt", "a")
while True:
    line = input("gimme some text to put into the file: ")
    if line.lower()== "stop":
            break
    f.write(line + "\n")


f.close()