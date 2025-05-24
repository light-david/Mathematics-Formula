class Fraction_Rules:
    def __init__(self):
        self.rules = {
            "addition": "To add fractions, find a common denominator, convert the fractions, and then add the numerators.",
            "subtraction": "To subtract fractions, find a common denominator, convert the fractions, and then subtract the numerators.",
            "multiplication": "To multiply fractions, multiply the numerators together and the denominators together.",
            "division": "To divide fractions, multiply by the reciprocal of the second fraction."
        }

    def get_rule(self, operation):
        return self.rules.get(operation.lower(), "Rule not found.")
    
    def add_fractions(self, num1, den1, num2, den2):
        if den1 == 0 or den2 == 0:
            return "Math Error: Division by zero"
        common_denominator = den1 * den2
        new_num1 = num1 * den2
        new_num2 = num2 * den1
        result_num = new_num1 + new_num2
        return result_num, common_denominator
    
    def subtract_fractions(self, num1, den1, num2, den2):
        common_denominator = den1 * den2
        new_num1 = num1 * den2
        new_num2 = num2 * den1
        result_num = new_num1 - new_num2
        return result_num, common_denominator
    
    def multiply_fractions(self, num1, den1, num2, den2):
        result_num = num1 * num2
        result_den = den1 * den2
        return result_num, result_den
    
    def divide_fractions(self, num1, den1, num2, den2):
        if num2 == 0:
            return "Math Error: Division by zero"
        result_num = num1 * den2
        result_den = den1 * num2
        return result_num, result_den

if __name__ == "__main__":
    fraction_rules = Fraction_Rules()
    
    # Example usage
    print(fraction_rules.get_rule("addition"))
    print(fraction_rules.add_fractions(1, 2, 1, 3))  # (5, 6)
    print(fraction_rules.subtract_fractions(1, 2, 1, 3))  # (1, 6)
    print(fraction_rules.multiply_fractions(1, 2, 1, 3))  # (1, 6)
    print(fraction_rules.divide_fractions(1, 2, 1, 3))  # (3, 2)
    print(fraction_rules.divide_fractions(1, 2, 0, 3))  # Math Error: Division by zero