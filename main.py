import cash
import sys

def main():
    amountToReturn = int(sys.argv[1])
    cashManager = cash.CashManager()
    print(cashManager.change(amountToReturn))

if __name__ == "__main__":
    main()