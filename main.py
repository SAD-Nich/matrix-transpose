mx = eval(input("Enter a Matrix: "))
rst = [[mx[n][m] for n in range(len(mx))] for m in range(len(mx[0]))]
print("This is the result", rst)