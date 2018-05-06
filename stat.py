def mean(values):
    """Calculate the mean of given values

    >>> mean((1, 2, 3))
    2.0

    >>> mean([1.0, 2, 3])
    2.0

    >>> mean({1: 'asd', 2: 2, 3: []})
    2.0

    Args:
        values (iterable of numbers): the values that you want the mean from
    Returns:
        the mean of given values (total_sum/qtd_values)
    Raises:
        ZeroDivisionError: if no value is passed
        TypeError: if any value of iterable isnt a number
    """
    return float(sum(values))/len(values)

def mode(values):
    """Calculate the most common value from iterable

    >>> mode([1, 2, 3, 2])
    set([2])

    >>> mode([(4, 4, 4), "mother", "mother", 3, 3])
    set(['mother', 3])

    Args:
        values (iterable): the values that you want the mode
    Returns:
        a set with the values that appears the most
    """
    freq = abs_frequence(values)
    maior = 0
    for v in values:
        maior = max(maior, freq[v])

    res = set()
    for v in freq:
        if freq[v] == maior:
            res.add(v)

    return res

def abs_frequence(values):
    freq = {}
    for v in values:
        if v in freq:
            freq[v] += 1
        else:
            freq[v] = 1
    return freq

def rel_frequence(values):
    total = len(values)
    freq = {}
    for v in values:
        if v in freq:
            freq[v] += 1.0/total
        else:
            freq[v] = 1.0/total
    return freq

def percentage(values):
    total = len(values)
    freq = {}
    for v in values:
        if v in freq:
            freq[v] += 100.0/total
        else:
            freq[v] = 100.0/total
    return freq

'''
data = [12, 15, 18, 15, 12, 18, 18, 15, 18, 17, 19, 20]
print abs_frequence(data)
print rel_frequence(data)
print percentage(data)
'''
