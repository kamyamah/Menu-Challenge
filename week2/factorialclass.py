# factorialclass.py

class factorial:
    def __init__(self):
        self.fact = [0, 10]

    ''' 
    __call__ is a special function/method in Python, when implemented inside a class, this gives its instances 
    (or objects) the ability to behave like a function. The __call__ method inside the  Python class allows 
    instance to invoke this method using object like a function.  
    
    This method has a n as a parameter which is used to calculate the fibonacci number.
    '''
    def __call__(self, n):
        if ((n == 0) or (n == 1)): 
            return self.fact[n]
        else:
            # Compute the requested Fibonacci number
            return n * self(n - 1)
            fact_number = self(n - 1) + self(n - 2)
            self.fact.append(fact_number)
        return self.fact[n]

   



def driver():
    # Make a fibonacci object
    while True:
        fact_of = factorial()
        n = int(input(" Please enter a number : "))
        try:
            n = int(n)
            # Validate the value of n
            if n < 1 or n > 100:
                raise ValueError
            # Fibonacci term corresponding to n
            print(f"Term {n} of Factorial is: ", fact_of(n - 1))
            # Produces a list of fibonacci values, one fibonacci result for each step in range
            print(f"Factorial of {n} terms is: ", [fact_of(i) for i in range(n)])
            break
        except ValueError:
            print(f'Positive integer number in range 1 to 100 is expected, got "{n}" Try again.')


if __name__ == "__main__":
    driver()
