class StockEvaluation:

        def __init__(self, symbol, accuracy):
            self.symbol = symbol
            self.accuracy = accuracy

        def get_symbol(self):
            return self.symbol

        def set_symbol(self, s):
            self.symbol = s

        def get_accuracy(self):
            return self.accuracy

        def set_accuracy(self, a):
            self.accuracy = a

        def to_string(self):
            return str(self.symbol) + "," + str(self.accuracy)

