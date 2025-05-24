class SimpleInterest:
    def __init__(self, principal: float, rate: float, time: float):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate(self) -> float:
        """
        Calculate the simple interest.

        Returns:
            float: The calculated simple interest.
        """
        return (self.principal * self.rate * self.time) / 100

    def __str__(self) -> str:
        return f"Simple Interest: {self.calculate()}"
    
    def __repr__(self) -> str:
        return f"SimpleInterest(principal={self.principal}, rate={self.rate}, time={self.time})"

if __name__ == "__main__":
    principal = 1000.0  # Principal amount
    rate = 5.0          # Rate of interest per annum
    time = 3.0          # Time in years

    si = SimpleInterest(principal, rate, time)
    print(si)  # Output: Simple Interest: 150.0
    print(repr(si))  # Output: SimpleInterest(principal=1000.0, rate=5.0, time=3.0)
    print("Calculated Simple Interest:", si.calculate())  # Output: 150.0
# This code defines a SimpleInterest class that calculates simple interest based on the principal amount, rate of interest, and time period.