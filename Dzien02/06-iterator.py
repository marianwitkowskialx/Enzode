
# Iterator
from collections.abc import Iterator, Iterable

class WordsIterator(Iterator):
    def __init__(self, words):
        self._words = words
        self._position = 0

    def __next__(self):
        try:
            value = self._words[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()
        return value

class WordsCollection(Iterable):
    def __init__(self):
        self._words = []

    def __iter__(self):
        return WordsIterator(self._words)

    def add_item(self, item):
        self._words.append(item)

###
# collection = WordsCollection()
# collection.add_item("Ala")
# collection.add_item("ma")
# collection.add_item("kota")

collection = WordsIterator(["Ala", "ma", "kota"])
for c in collection:
    print(c)

#print("\n".join(collection))


