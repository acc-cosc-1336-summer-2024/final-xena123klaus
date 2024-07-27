def create_multiplication_table():
    table = []
    for i in range(1, 6):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        print(" ".join(map(str, row)))

def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)

        user_input = input("Do you want to create another table? (yes/no): ").strip().lower()
        if user_input != 'yes':
            print("Goodbye!")
            break
