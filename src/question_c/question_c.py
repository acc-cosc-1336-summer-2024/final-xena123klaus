
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
        aapl.get_symbol(): aapl.get_company_name(),
        cat.get_symbol(): cat.get_company_name(),
        ek.get_symbol(): ek.get_company_name(),
        goog.get_symbol(): goog.get_company_name(),
        msft.get_symbol(): msft.get_company_name()
    }
    return stocks


def main():
    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            history = stock_purchase_history()
            print("Stock Purchase History:")
            for symbol, company in history.items():
                print(f"Symbol: {symbol}, Company: {company}")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
