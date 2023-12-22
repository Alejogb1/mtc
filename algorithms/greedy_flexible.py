class Item(object):
    def __init__(self, n, v, w):
        self._name = n
        self._value = v
        self._weight = w
    def get_name(self):
        return self._name
    def get_value(self):
        return self._value
    def get_weight(self):
        return self._weight
    def __str__(self):
        return f'<{self._name},   {self._value}, {self._weight}>'


def value(item):
    return item.get_value()

def weight_inverse(item):
    return 1.0/item.get_weight()

def density(item):
    return item.get_value()/item.get_weight()

def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse=True)

    # (We use sorted rather than sort because 
    # we want to generate a new list rather than mutate the list passed to the function.)

    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].get_weight()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].get_weight()
            totalValue += itemsCopy[i].get_value()

    return (result, totalValue)