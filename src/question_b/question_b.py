def create_multiplication_table():
    table = []
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        print(" ".join(f"{num:2}" for num in row))

def main():
    while True:
        print("\nMenu:")
        print("1 - Display multiplication table")
        print("2 - Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            table = create_multiplication_table()
            display_multiplication_table(table)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")





