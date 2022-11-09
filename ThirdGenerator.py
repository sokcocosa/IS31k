class CustomRandom:
    @staticmethod
    def Sum():
        a = float(input('a: '))
        b = float(input('b: '))
        return a + b


if __name__ == '__main__':
    print("Sum")
    print(CustomRandom.Sum())
