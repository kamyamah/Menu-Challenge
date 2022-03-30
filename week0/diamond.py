def diamond():
  
  n = 9
  print("Pattern 1")
  for a1 in range(1, (n+1)//2): #from row 1 to 5
      for a2 in range((n+1)//2 - a1):
          print(" ", end = "")
      for a3 in range((a1*2)-1):
          print("*", end = "")
      print()
  
  for a1 in range((n+1)//2 + 1, n + 1): #from row 6 to 9
      for a2 in range(a1 - (n+1)//2):
          print(" ", end = "")
      for a3 in range((n+1 - a1)*2 - 1):
          print("*", end = "")
      print()

  if __name__=='__main__':
    # print_menu1()
      diamond()