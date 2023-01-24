# Print every number between 1 and 100 as follows:
#
# For every multiple of 3 print "Three".
# For every multiple of 5 print "Five".
# And for every multiple of both 3 and 5 print "ThreeFive"

for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("ThreeFive")
    elif i % 3 == 0:
        print("Three")
    elif i % 5 == 0:
        print("Five")
    else:
        print(i)

