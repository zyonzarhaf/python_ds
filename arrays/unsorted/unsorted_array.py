from arrays.core import Array


class UnsortedArray:
    def __init__(self, max_size, typecode='1'):
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        self._size = 0

    def insert(self, new_entry):
        if self._size >= len(self._array):
            raise ValueError('Array already at full capacity.')
        else:
            self._array[self._size] = new_entry
            self._size += 1

    def delete(self, index):
        if self._size == 0:
            raise ValueError('Delete from an empty array.')
        elif index < 0 or index >= self._size:
            raise ValueError(f'Index {index} out of range.')
        else:
            self._array[index] = self._array[self._size-1]
            self._size -= 1

    def find(self, target):
        for index in range(0, self._size):
            if self._array[index] == target:
                return index
        return None

    def traverse(self, callback):
        for index in range(self._size):
            callback(self._array[index])
