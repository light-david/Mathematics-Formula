class Percentage:
    def __init__(self, value: float):
        self.value = value

    def of(self, total: float) -> float:
        """Calculate the percentage of a total."""
        if total == 0:
            raise ValueError("Total cannot be zero.")
        return (self.value / 100) * total

    def from_total(self, total: float) -> float:
        """Calculate what percentage this value is of a total."""
        if total == 0:
            raise ValueError("Total cannot be zero.")
        return (self.value / total) * 100
    
    def increase(self, total: float) -> float:
        """Calculate the increased value by this percentage of a total."""
        if total == 0:
            raise ValueError("Total cannot be zero.")
        return total + self.of(total)
    
    def decrease(self, total: float) -> float:
        """Calculate the decreased value by this percentage of a total."""
        if total == 0:
            raise ValueError("Total cannot be zero.")
        return total - self.of(total)
    
    def change(self, total: float) -> float:
        """Calculate the change in value by this percentage of a total."""
        if total == 0:
            raise ValueError("Total cannot be zero.")
        return self.of(total) - (total - self.of(total))
    
    def __str__(self):
        return f"{self.value}%"
    
    def __repr__(self):
        return f"Percentage(value={self.value})"

if __name__ == "__main__":
    p = Percentage(20)
    total = 200
    print(f"{p} of {total} is {p.of(total)}")
    print(f"{p} from {total} is {p.from_total(total)}%")
    print(f"Increasing {total} by {p} gives {p.increase(total)}")
    print(f"Decreasing {total} by {p} gives {p.decrease(total)}")
    print(f"Change in value by {p} of {total} is {p.change(total)}")