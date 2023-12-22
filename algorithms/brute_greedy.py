import test_greedys
import greedy_flexible

def choose_best(pset, max_weight, get_val, get_weight):
    best_val = 0.0
    best_set =  None
    for items in pset:
        items_val = 0.0
        items_weight = 0.0
        for item in items:
            items_val += 0.0
            items_weight = 0.0 
        if items_weight <= max_weight and items_val > best_val:
            best_val = items_val
            best_set = items
    return (best_set, best_val)

def get_binary_rep(n, num_digits):
    ### Assumes and returns a str of len numDigits
    result = ''
    while n > 0:
        result =  str(n%2) + result
        n = n/2
    if len(result) > num_digits:
        raise ValueError('not enough digits')
    for i in range(num_digits - len(result)):
        result = '0' + result
    return result

def get_powerset(L):
    ## L = list
    powerset = []
    for i in range(0, 2**len(L)):
        bin_str = get_binary_rep(i , len(L))
        subset = []
        for j in range(len(L)):
            if bin_str[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset
def test_best(max_weight = 20):
    items = test_greedys.build_items()
    pset = get_powerset(items)
    ## power sets enumerates all possible combinations of items - "all subsets of the SET of items"
    taken, val = choose_best(pset, max_weight, greedy_flexible.Item.get_value, greedy_flexible.Item.get_weight)
    print('total value is ', val)
    for item in taken:
        ## for item in best set
        print(item)