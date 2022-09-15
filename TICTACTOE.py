def get_row_col(string):
    for letter in string:
        print(type(letter))
        if letter == "A":
            col=0
        elif letter == "B":
            col=1
        elif letter == "C":
            col=2
        if letter == "1":
            row=0
        elif letter == "2":
            row=1
        elif letter == "3":
            row=2
    tup = (row, col)
    return(tup)
print(get_row_col("C1"))
