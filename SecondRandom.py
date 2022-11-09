import random


class CustomRandom:
    @staticmethod
    def negativeRandom():
        return -1 * random.randint(0, 100)


if __name__ == '__main__':
    print("Generate negative random value")
    print(CustomRandom.negativeRandom())
