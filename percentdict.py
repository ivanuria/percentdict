#!/usr/bin/env python3

from collections.abc import MutableMapping
from collections.abc import KeysView, ValuesView, ItemsView
from collections.abc import Iterable

class PercentDict(MutableMapping):
    def __init__(self, instance=None):
        self._mapping = [(1, None)] #By default everything is None
        if instance is not None:
            self.update(instance)

    def __contains__(self, item): # Checks values
        for i in self._mapping.copy():
            if item == i[1]:
                return True
        else:
            return False

    def __delitem__(self, key):
        value = self.get(key)
        for index, item in enumerate(self._mapping.copy()):
            if value == item[1]:
                del(self._mapping[index])
                break

    def __eq__(self, instance):
        if isinstance(instance, PercentDict):
            return self._mapping == instance._mapping
        else:
            return False            

    def __getitem__(self, key):
        return self.get(key)

    def __iter__(self):
        yield from self.keys()

    def __len__(self):
        return len(self._mapping)

    def __ne__(self, instance):
        return not self.__eq__(instance)

    def __setitem__(self, key, value):
        if isinstance(key, (float, int)):
            if key < 0 or key > 1:
                raise KeyError("Key must be a float between 0 and 1")
            final_index = None
            for index, item in enumerate(reversed(self._mapping)):
                if key == item[0]:
                    final_index = -(index+1)
                    break
            if final_index is not None:
                self._mapping[final_index] = (key, value)
            else:
                self._mapping.append((key, value))
                self._mapping.sort()

        elif isinstance(key, slice):
            if key.start < 0 or key.start > 1:
                raise KeyError("Keys must be a float between 0 and 1")
            if key.stop < 0 or key.stop > 1:
                raise KeyError("Keys must be a float between 0 and 1")
            end_index = None
            start_index = None
            start_value = None
            todel = []
            for index, item in enumerate(reversed(self._mapping)):
                if key.stop == item[0]:
                    end_index = -(index+1)
                    start_value = item[1]
                if key.start == item[0]:
                    start_index = -(index+1)
                    start_value = item[1]
                elif key.start < item[0] < key.stop:
                    start_value = item[1]
                    todel.append(item[0])
                elif key.start > item[0]:
                    break
                if end_index is not None and start_index is not None:
                    break
            if end_index is not None:
                self._mapping[end_index] = (key.stop, value)
            else:
                self._mapping.append((key.stop, value))
            if start_index is not None:
                self._mapping[start_index] = (key.start, start_value)
            else:
                self._mapping.append((key.start, start_value))
            for i in todel:
                if i != key.start and i != key.stop:
                    del(self[i])
            if end_index is None or start_index is None:
                self._mapping.sort()
    
    def clear(self):
        self._mapping = [(1, None)]

    def get(self, key):
        if isinstance(key, (float, int)):
            if key < 0 or 1 < key:
                raise KeyError("Key must be a float between 0 and 1")
            for item in self._mapping:
                print(f"{(key, item)}")
                if key <= item[0]:
                    return item[1]
            else:
                raise KeyError("Key not found. If this error is raised I'm a moron")
            
        elif isinstance(key, slice):
            final = []
            for item in reversed(self._mapping):
                if key.stop <= item[0] or key.start <= item[0]:
                    final.append(item[1])
                elif key.start > item[0]:
                    break
            if final:
                return tuple(final)
            else:
                raise KeyError()
        
        else:
            raise KeyError("Key must be a number or a slice")

    def items(self):
        return PercentItems(self)

    def keys(self):
        return PercentKeys(self)

    def pop(self):
        raise NotImplemented()

    def popitem(self):
        raise NotImplemented()

    def setdefault(self, default):
        raise NotImplemented()

    def update(self, instance):
        if isinstance(instance, PercentDict):
            self._mapping = instance._mapping
        elif isinstance(instance, Iterable):
            for index, item in enumerate(instance):
                if len(item) != 2:
                    raise ValueError(f"PercentDict update sequence element #{index} has length{len(item)}; 2 is required")
                else:
                    self.__setitem__(*item)
        else:
            raise ValueError(f"{type(instance)} is not iterable")
    
    def values(self):
        return PercentValues(self)

class PercentItems(ItemsView):
    def __init__(self, percentdict):
        if not isinstance(percentdict, PercentDict):
            raise ValueError("Requires PercentDict Instance")
        self._mapping = percentdict

    def __contains__(self, item):
        for i in self._mapping:
            if (i, self._mapping[i]) == item:
                return True
        else:
            return False

    def __iter__(self):
        for i in self._mapping:
            yield (i, self._mapping[i])

    def __len__(self):
        return len(self._mapping)

    def __reversed__(self):
        for i in reversed(self._mapping._mapping):
            yield i

class PercentKeys(KeysView):
    def __init__(self, percentdict):
        if not isinstance(percentdict, PercentDict):
            raise ValueError("Requires PercentDict Instance")
        self._mapping = percentdict

    def __contains__(self, item):
        for i in self._mapping._mapping:
            if i[0] == item:
                return True
        else:
            return False

    def __iter__(self):
        for i in self._mapping._mapping:
            yield i[0]

    def __len__(self):
        return len(self._mapping._mapping)

    def __reversed__(self):
        for i in reversed(self._mapping._mapping):
            yield i[0]

class PercentValues(ValuesView):
    def __init__(self, percentdict):
        if not isinstance(percentdict, PercentDict):
            raise ValueError("Requires PercentDict Instance")
        self._mapping = percentdict

    def __contains__(self, item):
        for i in self._mapping._mapping:
            if i[1] == item:
                return True
        else:
            return False

    def __iter__(self):
        for i in self._mapping._mapping:
            yield i[1]

    def __len__(self):
        return len(self._mapping._mapping)

    def __reversed__(self):
        for i in reversed(self._mapping._mapping):
            yield i[1]