def get_statistics(numbers):
    if len(numbers) != 5:
        raise ValueError("Exactly 5 numbers are required")
    
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return lowest, highest, total, average

def main():
    numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(5)]

    lowest, highest, total, average = get_statistics(numbers)

    print(f"\nLowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")

    