# write a program to append the times tables to our eminem.txt file

with open("eminem.txt", 'a') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{0} times {1:>2} is {2}".format(i, j, i*j), file=tables)
        print("_" * 20, file=tables)