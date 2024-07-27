def main():
    numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(5)]

    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print(f"\nLowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")

    