class properties_of_operations:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def commutative_property(a, b):
        """
        This function obeys the commutative property of operations
        """
        while True:
            a + b == b + a
            a * b == b * a
            return True
    
    def associative_property(a, b, c):
        """
        This function obeys the associative property of operations
        """
        while True:
            (a + b) + c == a + (b + c)
            (a * b) * c == a * (b * c)
            return True
        
    def distributive_property(a, b, c):
        """
        This function obeys the distributive property of operations
        """
        while True:
            a * (b + c) == a * b + a * c
            a * (b - c) == a * b - a * c
            return True
        
    def identity_property(a):
        """
        This function obeys the identity property of operations
        """
        while True:
            a + 0 == a
            a * 1 == a
            a - 0 == a
            a / 1 == a
            return True
        
    def inverse_property(a):
        """
        This function obeys the inverse property of operations
        """
        while a != 0:
            a + (-a) == 0
            a * (a**-1) == 1
            return True