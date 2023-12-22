import greedy_flexible



def build_items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(values)):
        Items.append(greedy_flexible.Item(names[i], values[i], weights[i]))
    return Items

def test_greedy(items, max_weight, key_function):
    taken, val = greedy_flexible.greedy(items, max_weight, key_function)
    print('total value is ', val)
    for item in taken:
        print(' ', item)
def test_greedys(max_weight = 20):
    items = build_items()
    print('Use greedy by value to fill size ', max_weight)
    test_greedy(items, max_weight, greedy_flexible.value)
    print('Use greedy by weight to fill size ', max_weight)
    test_greedy(items, max_weight, greedy_flexible.weight_inverse)
    print('Use greedy by density to fill size ', max_weight)
    test_greedy(items, max_weight, greedy_flexible.density)

test_greedys()
