for i in range(1, 11):
    for j in range(1, 11):
        # format each number in the table to take up 4 spaces
        print('{:4}'.format(i*j), end='')
    print()