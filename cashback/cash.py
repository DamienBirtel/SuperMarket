# _Coins is intended to be private and only used by CashManager
class _Coins:

    # _Coin holds two properties:
    #   - amount, which represents to smallest amount of coins needed to exactly add up to a given number,
    #       -1 means we can't do it given the types of coins we have
    #   - types, which represents the types of coins we can use to make change and the amount needed to do it
    def __init__(self, availableCoins):
        self.amount = -1
        self.types = {}
        for coin in availableCoins:
            self.types[coin] = 0


class CashManager:
    # CashManager takes a tuple of integers as parameters which represents the coins and notes we are able to return
    # We sort it in reversed order to allow an easier manipulation later
    def __init__(self, availableCoins=(10, 5, 2)):
        self.coinsAndNotes = sorted(availableCoins, reverse=True)


    # change takes an integer amountToReturn as a paramter and returns a dictionary where 
    # the keys are the types of coins and the values are the amount of coins to add up to amountToReturn
    # or returns None if it can't find an exact combination of coins to get to amountToReturn
    def change(self, amountToReturn=0):

        # To find which coins to use to have the smallest amount of coins for amountToReturn we first
        # need to find every smallest amount of coins for every number up to amountToReturn so
        # we create a list of _Coins which will hold information for that
        combinations = [_Coins(self.coinsAndNotes) for x in range(amountToReturn + 1)]

        # We set the first amount of coins to 0 as we need 0 coin to give back 0 change
        combinations[0].amount = 0

        # We loop through every amount
        for amount, combination in enumerate(combinations):

            # We loop through every coin from highest to lowest
            for coin in self.coinsAndNotes:

                # We check if we can use the coin as it needs to be lower than amountToReturn
                # and if it is higher, remainder needs to already have a solution
                remainder = amount - coin
                if remainder >= 0 and combinations[remainder].amount > -1:

                    # we add one coin to the amount needed for the solved remainder
                    combination.amount = combinations[remainder].amount + 1

                    # we copy which coins we needed for the solved remainder
                    combination.types = combinations[remainder].types.copy()

                    # we add the current tested coin to the dictionary
                    combination.types[coin] += 1

                    # we break as soon as we find a solution since we check from highest to lowest coin types
                    break 

        # we return None if we couldn't find a combination
        if combinations[amountToReturn].amount == -1:
            return None

        # we return the dictionary holding the information about which amount of which coins to use
        return combinations[amountToReturn].types

                    
        
        
