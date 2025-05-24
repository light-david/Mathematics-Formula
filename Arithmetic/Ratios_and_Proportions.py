class RatiosAndProportions:
    def __init__(self):
        self.ratios_list = []
        self.proportions_list = []
    
    def add_ratio(self, ratio):
        """Add a ratio to the list."""
        if isinstance(ratio, (list, tuple)) and len(ratio) == 2:
            self.ratios_list.append(ratio)
        else:
            raise ValueError("Ratio must be a list or tuple of two numbers.")
    
    def add_proportion(self, proportion):
        """Add a proportion to the list."""
        if isinstance(proportion, (list, tuple)) and len(proportion) == 2:
            self.proportions_list.append(proportion)
        else:
            raise ValueError("Proportion must be a list or tuple of two numbers.")
    
    def calculate_ratio(self, ratio):
        """Calculate the ratio of two numbers."""
        if len(ratio) != 2:
            raise ValueError("Ratio must contain exactly two numbers.")
        return ratio[0] / ratio[1] if ratio[1] != 0 else "Undefined (division by zero)"
    
    def calculate_proportion(self, proportion):
        """Calculate the proportion of two numbers."""
        if len(proportion) != 2:
            raise ValueError("Proportion must contain exactly two numbers.")
        return proportion[0] / proportion[1] if proportion[1] != 0 else "Undefined (division by zero)"
    
    def check_proportionality(self, a, b, c, d):
        """Check if two ratios are proportional."""
        if b == 0 or d == 0:
            return "Undefined (division by zero)"
        return (a / b) == (c / d)
    
    def __str__(self):  
        return f"Ratios: {self.ratios_list}, Proportions: {self.proportions_list}"
    
    def __repr__(self):
        return f"RatiosAndProportions(ratios={self.ratios_list}, proportions={self.proportions_list})"

if __name__ == "__main__":
    rp = RatiosAndProportions()
    rp.add_ratio((3, 4))
    rp.add_ratio((5, 10))
    rp.add_proportion((2, 3))
    rp.add_proportion((4, 6))
    
    print("Ratios:", rp.ratios_list)
    print("Proportions:", rp.proportions_list)
    
    ratio_result = rp.calculate_ratio((3, 4))
    print("Calculated Ratio (3:4):", ratio_result)
    
    proportion_result = rp.calculate_proportion((2, 3))
    print("Calculated Proportion (2:3):", proportion_result)
    
    proportionality_check = rp.check_proportionality(1, 2, 2, 4)
    print("Are (1:2) and (2:4) proportional?", proportionality_check)
    proportionality_check = rp.check_proportionality(1, 2, 2, 5)
    print("Are (1:2) and (2:5) proportional?", proportionality_check)