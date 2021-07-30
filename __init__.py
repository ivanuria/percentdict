#!/usr/bin/env python3

from collections.abc import MutableMapping, KeysView, ValuesView, ItemsView

class PercentKeys(KeysView):
    def __init__(self, percentdict):
        self._percentdict = percentdict

    def __contains__(self, item):
        pass

    def __iter__(self):
        pass

    def len(self):
        pass

    def reversed(self):
        pass

class PercentValues(ValuesView):
    def __init__(self, percentdict):
        self._percentdict = percentdict

    def __contains__(self, item):
        pass

    def __iter__(self):
        pass

    def len(self):
        pass

    def reversed(self):
        pass

class PercentItems(ValuesView):
    def __init__(self, percentdict):
        self._percentdict = percentdict

    def __contains__(self, item):
        pass

    def __iter__(self):
        pass

    def len(self):
        pass

    def reversed(self):
        pass 

class PercentDict(MutableMapping):
    def __init__(self, instance=None):
        self._keys = []
        self._values = []

    def __contains__(self, item):
        pass

    def __delitem__(self, key):
        pass

    def __eq__(self, instance):
        pass

    def __getitem__(self, key):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __ne__(self, instance):
        pass

    def __setitem__(self, key, value):
        pass
    
    def clear(self):
        pass

    def get(self):
        pass

    def items(self):
        pass

    def keys(self):
        pass

    def pop(self):
        raise NotImplemented()

    def popitem(self):
        raise NotImplemented()

    def setdefault(self, default):
        pass

    def update(self, instance):
        pass
    
    def values(self):
        pass