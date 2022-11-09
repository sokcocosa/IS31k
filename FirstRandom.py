import random


class CustomRandom:
    @staticmethod
    def positiveRandom():
        return random.randint(0, 100)


if __name__ == '__main__':
    print("Generate positive random value")
    print(CustomRandom.positiveRandom())

