#A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. A prime number is only divisible by 1 and itself. The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, and so on.
#So prime number can only be formed by multiplying 1 and itself.

class Prime:
    def __init__(self, number):
        self.number = number
        
    def is_prime(self):
        if self.number <= 1:
            return False
        