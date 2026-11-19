class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def show(self):
        print("Current value:", self.value)

counter1 = Counter()
counter2 = Counter()

counter1.increment()
counter1.increment()
counter2.increment()

counter1.show()
counter2.show()