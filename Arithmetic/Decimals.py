class Decimals_Rule:
    def __init__(self):
        self.rule = {
            "Addition": "When adding decimals, align the decimal points and add as you would with whole numbers.",
            "Subtraction": "When subtracting decimals, align the decimal points and subtract as you would with whole numbers.",
            "Multiplication": "Multiply as if there are no decimal points, then count the total number of decimal places in both factors and place the decimal point in the product accordingly.",
            "Division": "Move the decimal point in the divisor to make it a whole number, then move the decimal point in the dividend the same number of places. Divide as you would with whole numbers."
        }
    
    def get_rule(self, operation):
        return self.rule.get(operation, "Rule not found for this operation.")

if __name__ == "__main__":
    decimals_rule = Decimals_Rule()
    print("Addition Rule:", decimals_rule.get_rule("Addition"))
    print("Subtraction Rule:", decimals_rule.get_rule("Subtraction"))
    print("Multiplication Rule:", decimals_rule.get_rule("Multiplication"))
    print("Division Rule:", decimals_rule.get_rule("Division"))
    print("Invalid Operation Rule:", decimals_rule.get_rule("Invalid"))