from calculator import Calculator
from composer import compose

if __name__ == '__main__':
    exp = input('write an expression: ')
    exp = compose(exp)
    try:
        calc = Calculator(exp)
        print(calc.calculate())
    except Exception as e:
        print(f' Error {e} '.center(50, '-'))
