class Calc:
    # create class
    # The class is a simple calculator
    def __init__(self):
        # a class without initial data
        self.result = 0

    def addition(self, a, b):
        # the adding operation is performed
        self.result = a + b
        pass

    def subtraction(self, a, b):
        # the subtraction operation is performed
        self.result = a - b
        pass

    def multiplication(self, a, b):
        # the multiplication operation is performed
        self.result = a * b
        pass

    def division(self, a, b):
        # the division operation is performed
        self.result = a / b
        pass

if __name__ == '__main__':
    # start only on compile this page
    local_calc = Calc()
    # checking the initial parameters
    print(local_calc.result)
    # checking the creation of a class object
    print(local_calc)
    # performing the addition action
    local_calc.addition(4, 5)
    # we are looking at the result of the addition
    print(local_calc.result)
    # performing the multiplication operation
    local_calc.multiplication(4, 5)
    # we are looking at the multiplication result
    print(local_calc.result)