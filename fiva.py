j = 5
for i in range(7, 0 - 1, -1):
    if i == 0:
        print "000"
    else:
        print "{}{}".format(i * 111, j if j >= 0 else "")
    j -= 1