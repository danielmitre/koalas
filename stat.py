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


def median(values):
    """Calculate a value that puts half of values at its left

    >>> median([1, 2, 3, 4])
    2.5

    >>> median([1, 2, 3])
    2

    >>> median([4, 1, 5, 2])
    3.0

    Args:
        Values (iterable of numbers): the values that you want the median
    Returns:
        A real number that represents the median of values.
    Raises:
        IndexError: if values is passed as a empty iterator
    """
    values = sorted(values)
    tam = len(values)
    if tam%2 == 1:
        return values[(tam-1)/2]
    half = tam/2
    return (values[half] + values[half-1]) / 2.0
