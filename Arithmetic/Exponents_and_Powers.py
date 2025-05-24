class ExponentsAndPowers:
    def __init__(self, a, b, c, expression):
        self.a = a
        self.b = b
        self.c = c
        if "^" in expression:
            self.expression = expression.replace("^", "**")
            self.expression_result = eval(self.expression)
        else:
            self.expression = expression
            self.expression_result = None

    def multiply_exponents(self):
        # (a^c) * (a^b) = a^(b+c)
        return (self.a ** self.c) * (self.a ** self.b)

    def divide_exponents(self):
        # (a^b) / (a^c) = a^(b-c)
        return (self.a ** self.b) / (self.a ** self.c)

    def power_of_exponent(self):
        # (a^b)^c = a^(b*c)
        return (self.a ** self.b) ** self.c

    def exponent_of_zero(self):
        if self.a == 0:
            return "Math Error"
        else:
            return self.a ** 0

    def negative_exponent(self):
        if self.a == 0:
            return "Math Error"
        return self.a ** -self.b

if __name__ == "__main__":
    a = 2
    b = 3
    c = 4
    expression = "2^3"
    exp = ExponentsAndPowers(a, b, c, expression)
    print("Multiply Exponents:", exp.multiply_exponents())
    print("Divide Exponents:", exp.divide_exponents())
    print("Power of Exponent:", exp.power_of_exponent())
    print("Exponent of Zero:", exp.exponent_of_zero())
    print("Negative Exponent:", exp.negative_exponent())
    print("Expression:", expression)
    print("Expression Result:", exp.expression_result)