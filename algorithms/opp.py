import binary_search

answer = binary_search.binarySearch([12, 3, 6, 9, 0], 3, 0, len([12, 3, 6, 9, 0])-1)
print(answer)
print(__name__)

class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


damn = Numbers()
myiter = iter(damn)

print(next(myiter))
print(next(myiter))
print(next(myiter))

print(sum([int(input()) for i in range(3)]))
