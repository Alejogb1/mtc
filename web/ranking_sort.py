def score(item_votes):
    pretend_votes = [2,2,2,2,2,2]
    ## in a hypothetical world, either you don't like something at all, or you really LIKE it
    utilities = [-30, 1, 2, 3, 4, 70]
    votes = [iv+pv for (iv, pv) in zip(item_votes,pretend_votes)]
    ## zip generate tuples between first and second args
    return sum(v*u for (v,u) in zip(votes, utilities))/float(sum(votes))