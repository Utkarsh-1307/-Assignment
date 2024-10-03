class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._index = 0  # Keeps track of iteration

    def __iter__(self):
        # Reset index whenever a new iteration starts
        self._index = 0
        return self

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        else:
            raise StopIteration  # End of iteration


rect = Rectangle(10, 5)

# Iterating over the rectangle object
for value in rect:
    print(value)
