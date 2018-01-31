testcase = input()

i = 1;

while (i<=int(testcase)):
    year = input()

    if (int(year) < 2015):
        print(str(2015-int(year)) + " D.C.")
    else:
        print(str(int(year)-2014) + " A.C.")

    i = i+1