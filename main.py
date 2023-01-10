from calculator import Calculator
from composer import compose

start = True
if __name__ == '__main__':
    while start:
        exp = input('write an expression: ')
        if exp.strip() == "exit":
            start = False
            print("terminated sucessfully")
            break
        exp = compose(exp)
        try:
            calc = Calculator(exp)
            print(calc.calculate())
        except Exception as e:
            print(f' Error {e} '.center(50, '-'))
        finally:
            print('write exit and press enter to terminate')
