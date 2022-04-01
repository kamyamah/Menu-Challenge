def matrix():
  
  M1 = [[8, 14, -6],
           [12,7,4], 
           [-11,3,21]]

  matrix_length = len(M1)

  #To read the last element from each row.
  for i in range(matrix_length):
    print(M1[i][-1])

  if __name__ == "__main__":
    matrix()