class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Cannot deposit more than jar capacity")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies to withdraw")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 or size > self.capacity:
            raise ValueError("Size must be non-negative and within jar capacity")
        self._size = size

# Your main function remains the same


def main():
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()
