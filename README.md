# SuperMarket

This is a simple project which implements a CashManager class which, given a list of coins,
will return a dictionary containing what coins and how many of them to use to give back a certain amount of change.

### Usage

To test this you can use the main at your disposal and pass the amount of change you want to compute as first argument.
Examples:
```
$ python main.py 3
$ None
```
```
$ python main.py 11
$ {10: 0, 5: 1, 2: 3}
```

### Ideas to improve

- optimize algo for very high change
- tests
- better data management
