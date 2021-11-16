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
    # CashManager takes a dictionary of numbers represented with integers as key and strings as values
    def __init__(self, availableCoins={10:"ten", 5:"five", 2:"two"}):
        self.coinsAndNotes = []
        self.availableCoins = availableCoins
        self.returnDictionary = {}
        for key, value in availableCoins.items():
            self.coinsAndNotes.append(key)
            self.returnDictionary[value] = 0
        self.coinsAndNotes = sorted(self.coinsAndNotes, reverse=True)

    def _modulo(self, amountToReturn, coin):
        if amountToReturn % coin != 0:
            return None
        change = amountToReturn // coin
        self.returnDictionary[self.availableCoins[coin]] = change
        return self.returnDictionary

    def _contains_odd_coin(self):
        for coin in self.coinsAndNotes:
            if coin % 2 == 0:
                return True
        return False

    def _return_dictionary(self, dict):
        for key, value in dict.items():
            self.returnDictionary[self.availableCoins[key]] = value
        return self.returnDictionary

    # change takes an integer amountToReturn as a paramter and returns a dictionary where 
    # the keys are the types of coins and the values are the amount of coins to add up to amountToReturn
    # or returns None if it can't find an exact combination of coins to get to amountToReturn
    def change(self, amountToReturn=0):

        if len(self.coinsAndNotes) == 0 :
            return None

        if len(self.coinsAndNotes) == 1:
            return self._modulo(amountToReturn, self.coinsAndNotes[0])

        if amountToReturn % 2 != 0 and not self._contains_odd_coin():
            return None

        # To find which coins to use to have the smallest amount of coins for amountToReturn we first
        # need to find every smallest amount of coins for every number up to amountToReturn so
        # we create a list of _Coins which will hold information for that
        combinations = [_Coins(self.coinsAndNotes) for _ in range(amountToReturn + 1)]

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
        return self._return_dictionary(combinations[amountToReturn].types)

                    
        
        
