

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
def stock_purchase_history():
    aapl = Stock("AAPL", "Apple Inc")
    cat = Stock("CAT", "Caterpillar")
    ek = Stock("EK", "Eastman Kodak")
    goog = Stock("GOOG", "Google")
    msft = Stock("MSFT", "Microsoft")

    stocks = {
        aapl.get_symbol(): aapl,
        cat.get_symbol(): cat,
        ek.get_symbol(): ek,
        goog.get_symbol(): goog,
        msft.get_symbol(): msft
    }

    print("Stock Purchase History:")
    for symbol, stock in stocks.items():
        print(f"Symbol: {stock.get_symbol()}, Company: {stock.get_company_name()}")

def main():
    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            stock_purchase_history()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
