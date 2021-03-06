# percentdict

`PercentDict` offers a dict like object that gives you a way to implement a selector between two values. This value is a float between 0 and 1. 

To instantiate is so simple as:

```
pd = PercentDict()
```

Given the typical RPG table for throwing a d10. Step is not used in slices here:

```
1 -> You PC is poor
2-3 -> Your PC can survive
4-7 -> Your PC is middle class
8-9 -> Your PC is rich
10 -> Your PC is millionare
```

You can give the data this way:

```
pd[0:0.1] = "You PC is poor"
pd[0.1:0.3] = "Your PC can survive"
pd[0.3:0.7] = "Your PC is middle class"
pd[0.7:0.9] = "Your PC is rich"
pd[1] = "Your PC is millionaire"
```

The inferior limit will be used as superior limit of the previous one, so:

```
pd[0.1]
"You PC is poor"

pd[0.15]
"Your PC can survive"
```

You can fill those beginning only setting the max value:

```
pd[0.1] = "You PC is poor"
pd[0.3] = "Your PC can survive"
pd[0.7] = "Your PC is middle class"
pd[0.9] = "Your PC is rich"
pd[1] = "Your PC is millionaire"
```

I.E:

```
pd[0.15]
"Your PC can survive"
```

In case you'll use random library and you want to be sure the usage is similar to throwing a d10 like the example, use random.randint and divide it by the number of faces of the die. 10 in case of the example.

I.E:

```
pd[random.randint(10)/10]
```

You can use other dict methods, like `keys()`, `values()`... But `pop`, `popitem` and `setdefault` are not implemented because they make no sense.

For a more intuitive implementation in case you want to use like the example a dice like, you can use `RangedDict`. It will only accept integers in getters, setters and slices.

I.E:

```
rd = RangedDict(d=12) # d means the faces of the dice

rd[1] = "You PC is poor"
rd[2:4] = "Your PC can survive"
rd[5:9] = "Your PC is middle class"
rd[10:11] = "Your PC is rich"
rd[12] = "Your PC is millionaire"

rd[6]
"Your PC is middle class"
```

You can use the method `random()` to get a randomized value.

```
rd.random()
```

## Instalation
You can install with a simple

```
pip install percentdict
```
