def turtle():
   # replace *s with a space in a rowsxrows matrix
    for i in range(1,10):
        for j in range(0, 1-i):
            print(end=' ')
        for k in range(0, i):
            print('*', end=' ')
        for m in range(0, 1+i):
            print(end='')
        print()
    


if __name__ == "__main__":
    turtle()