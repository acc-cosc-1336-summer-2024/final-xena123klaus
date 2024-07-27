#write functions here, don't add input('') statements here!
class Stock:
    def __init__(stock_instance, symbol, company_name):
        stock_instance.__symbol = symbol
        stock_instance.__company_name = company_name

    def get_symbol(stock_instance):
        return stock_instance.__symbol
    
    def get_company_name(stock_instance):
        return stock_instance.__company_name
    
def main():
    microsoft_stock = Stock("MSFT", "Microsoft")

    print(f"Company: {microsoft_stock.get_company_name()}")
    print(f"Symbol: {microsoft_stock.get_symbol()}")

    





