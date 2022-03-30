import math
def imperative():
  base_number = float(input("Enter the base number"))
  exponent = float(input("Enter the exponent"))
  power = math.pow(base_number,exponent)
  print("Power is =",power)
  if __name__=='__main__':
      # print_menu1()
        imperative()