class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self.capacity = capacity
        self.cookies = []

    def __str__(self):
        return "🍪" * len(self.cookies)

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to deposite must be non-negative")
        if len(self.cookies) + n > self.capacity:
            raise ValueError("Exceed capacity")
        self.cookies.extend(["🍪"] * n)

    def withdraw(self, n):
        if isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to withdraw must be non-negative")
        if n > len(self.cookies):
            raise ValueError("Not enough cookies")
        self.cookies = self.cookies[:-n]


    @property
    def size(self):
        return len(self.cookies)
