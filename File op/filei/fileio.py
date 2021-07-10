# file = open("D:\Studies\Codevita2020\Digitpair.txt","r")
# for line in file:
#     print(line, end='')
#
# file.close()

# with open("D:\Studies\Codevita2020\Digitpair.txt","r") as file:
#     for line in file:
#         if "Digit" in line:
#             print(line)

# with open("D:\Studies\Codevita2020\Digitpair.txt","r") as file:
#     line = file.readline()
#     while line:
#         print(line, end=" ")
#         line = file.readline()

with open("D:\Studies\Codevita2020\Digitpair.txt","r") as file:
    lines = file.readlines()           #create a list of lines
print(lines, end=" ")

for line in lines:
    print(line, end=''             #actual text in the file


