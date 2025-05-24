class Average:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        """Add a number to the list."""
        if isinstance(number, (int, float)):
            self.numbers.append(number)
        else:
            raise ValueError("Number must be an integer or float.")

    def calculate_mean(self):
        """Calculate the mean (average) of the numbers."""
        if not self.numbers:
            return "No numbers to calculate mean."
        return sum(self.numbers) / len(self.numbers)

    def calculate_median(self):
        """Calculate the median of the numbers."""
        if not self.numbers:
            return "No numbers to calculate median."
        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        else:
            return sorted_numbers[mid]

    def calculate_mode(self):
        """Calculate the mode of the numbers."""
        if not self.numbers:
            return "No numbers to calculate mode."
        frequency = {}
        for number in self.numbers:
            frequency[number] = frequency.get(number, 0) + 1
        max_freq = max(frequency.values())
        modes = [num for num, freq in frequency.items() if freq == max_freq]
        return modes if len(modes) > 1 else modes[0]

    def clear_numbers(self):
        """Clear the list of numbers."""
        self.numbers = []

    def __str__(self):
        return f"Average(numbers={self.numbers})"

    def __repr__(self):
        return f"Average(numbers={self.numbers})"

if __name__ == "__main__":
    avg = Average()
    avg.add_number(10)
    avg.add_number(20)
    avg.add_number(30)
    avg.add_number(20)
    
    print("Numbers:", avg.numbers)
    print("Mean:", avg.calculate_mean())
    print("Median:", avg.calculate_median())
    print("Mode:", avg.calculate_mode())
    
    avg.clear_numbers()
    print("Numbers after clearing:", avg.numbers)
    avg.add_number(5)
    avg.add_number(15)
    avg.add_number(25)
    print("Numbers after adding new values:", avg.numbers)
    print("Mean after clearing and adding new values:", avg.calculate_mean())
    print("Median after clearing and adding new values:", avg.calculate_median())
    print("Mode after clearing and adding new values:", avg.calculate_mode())