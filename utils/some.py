

class Shape:

    def __init__(self, dimension):
        self.dimension = dimension

    def get_class(self):
        return "Shape"


class Rectangle(Shape):

    def __init__(self, dimension, length, breadth):
        super().__init__(dimension)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Square(Rectangle):

    def __init__(self, dimension, length):
        super().__init__(dimension, length, length)


square1 = Square("meter", 4)

# print(square1.area())
# print(square1.get_class())


# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Praful Parashar5:32 PM
# {'aet': ['eat', 'tea', 'ate']},
# {'ant': ['tan', 'nat']}


def anagram(lst):
    result = {}

    for word in lst:
        original = word[:]  # Copies
        # word = ""."(word.split()).sort()

        if word not in result:
            result[word] = []

        result[word].append(original)


def check_divider(function):
    def _check_divider(num, denom):
        if denom == 0:
            return 0

        return function(num, denom)

    return _check_divider


@check_divider
def divide(num, denom):
    return num / denom

print(divide(1, 2))


class PeopleRating:
    people = FK(related_name=)

People.objects.annotate(
    avg_ratings=Avg("ratings__rating")
).filter(avg_ratings__gte=5).values(
    "name", "avg_ratings"
)
