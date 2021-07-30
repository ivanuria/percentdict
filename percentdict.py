#!/usr/bin/env python3

from collections.abc import MutableMapping
from collections.abc import KeysView, ValuesView, ItemsView
from collections.abc import Iterable

class PercentDict(MutableMapping):
    def __init__(self, instance=None):
        if instance is not None:
            self._items = [(1, None)] #By default everything is None
        else:
            self.update(instance)

    def __contains__(self, item):
        for item in self._items.copy():
            if item == item[1]:
                return True
        else:
            return False

    def __delitem__(self, key): # It has more sense
        value = self.get(key)
        for index, item in enumerate(self._items.copy()):
            if value == item[1]:
                del(self._items[index])
                break

    def __eq__(self, instance):
        if isinstance(instance, PercentDict):
            return self._items == instance._items
        else:
            return False            

    def __getitem__(self, key):
        return self.get(key)

    def __iter__(self):
        yield from self.keys()

    def __len__(self):
        return len(self._items)

    def __ne__(self, instance):
        return not self.__eq__(instance)

    def __setitem__(self, key, value):
        if isinstance(key, float):
            if 0 > key > 1:
                raise KeyError("Key must be a float between 0 and 1")
            final_index = None
            for index, item in enumerate(reversed(self._items)):
                if key == item[0]:
                    final_index = -(index+1)
                    break
            if final_index is not None:
                self._items[final_index] = (key, value)
            else:
                self._items.append((key, value))
                self._items.sort()
    
    def clear(self):
        self._items = [(1, None)]

    def get(self, key):
        if isinstance(key, float):
            if 0 > key > 1:
                raise KeyError("Key must be a float between 0 and 1")
            for item in reversed(self._items):
                if key <= item[0]:
                    return item[1]
            else:
                raise KeyError("Key not found. If this error is raised I'm a moron")
            
        if isinstance(key, slice):
            final = []
            for item in reversed(self._items):
                if slice.end <= item[0] or slice.start <= item[0]:
                    final.append(item[1])
                elif slice.start > item[0]:
                    break
            if final:
                return tuple(final)
            else:
                raise KeyError()

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
            self._items = instance._items
        elif isinstance(instance, Iterable):
            for index, item in enumerate(instance):
                if len(item) != 2:
                    raise ValueError(f"PercentDict update sequence element #{index} has length{len(item)}; 2 is required")
                else:
                    self._items.__setitem__(*item)
        else:
            raise ValueError(f"{type(instance)} is not iterable")
    
    def values(self):
        return PercentValues(self)

class PercentItems(ItemsView):
    def __init__(self, percentdict):
        if not isinstance(percentdict, PercentDict):
            raise ValueError("Requires PercentDict Instance")
        self._pd = percentdict

    def __contains__(self, item):
        for i in self._pd._items:
            if i == item:
                return True
        else:
            return False

    def __iter__(self):
        for i in self._pd._items:
            yield i

    def len(self):
        return len(self._index)

    def reversed(self):
        for i in reversed(self._pd._items):
            yield i

class PercentKeys(KeysView):
    def __init__(self, percentdict):
        if not isinstance(percentdict, PercentDict):
            raise ValueError("Requires PercentDict Instance")
        self._pd = percentdict

    def __contains__(self, item):
        for i in self._pd._items:
            if i[0] == item:
                return True
        else:
            return False

    def __iter__(self):
        for i in self._pd._items:
            yield i[0]

    def len(self):
        return len(self._index)

    def reversed(self):
        for i in reversed(self._pd._items):
            yield i[0]

class PercentValues(ValuesView):
    def __init__(self, percentdict):
        if not isinstance(percentdict, PercentDict):
            raise ValueError("Requires PercentDict Instance")
        self._pd = percentdict

    def __contains__(self, item):
        for i in self._pd._items:
            if i[1] == item:
                return True
        else:
            return False

    def __iter__(self):
        for i in self._pd._items:
            yield i[1]

    def len(self):
        return len(self._index)

    def reversed(self):
        for i in reversed(self._pd._items):
            yield i[1]