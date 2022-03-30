import math
def exponent():
  base_number = float(input("Enter the base number: "))
  class exponent:
    def __init__(self):
      pass
    def __call__(self, base_number):
      exponent = float(input("Enter the exponent"))
      power = math.pow(base_number,exponent)
      print("Power is =",power)
  ans = exponent()
  ans(base_number)
