class calcolatore:
    def __init__(self):
        pass

    def somma(self, a, b):
        return a + b

    def divisione(self, a, b):
        if b == 0:
            raise ValueError("Divisione per zero non consentita.")
        return a / b