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
    """Calculate absolute frequence of elements

    >>> abs_frequence([1, 2, 3, 2])
    {1: 1, 2: 2, 3: 1}

    >>> abs_frequence([(4, 4, 4), "mother", "mother", 3, 3])
    {3: 2, 'mother': 2, (4, 4, 4): 1}

    Args:
        values (iterable): the values that you want the frequence
    Returns:
        a dict with the values and their frequence
    """
    freq = {}
    for v in values:
        if v in freq:
            freq[v] += 1
        else:
            freq[v] = 1
    return freq

def rel_frequence(values, multiplier=1.0):
    """Calculate relative frequence of elements

    >>> rel_frequence([1, 2, 3, 2])
    {1: 0.25, 2: 0.5, 3: 0.25}

    >>> rel_frequence([(4, 4, 4), "mother", "mother", 3, 3])
    {3: 0.4, 'mother': 0.4, (4, 4, 4): 0.2}

    Args:
        values (iterable): the values that you want the frequence
        [optional] multiplier (float): a value that shold multiply every frequence at the end
    Returns:
        a dict with the values and their frequence
    """
    total = len(values)
    freq = {}
    for v in values:
        if v in freq:
            freq[v] += multiplier/total
        else:
            freq[v] = multiplier/total
    return freq

def percentage(values):
    """Equivalent to rel_frequence(values, 100.0)

    >>> percentage([1, 2, 3, 2])
    {1: 25.0, 2: 50.0, 3: 25.0}

    >>> percentage([(4, 4, 4), "mother", "mother", 3, 3])
    {3: 40.0, 'mother': 40.0, (4, 4, 4): 20.0}

    Args:
        values (iterable): the values that you want the percentage of their frequence
    Returns:
        a dict with the values and their frequence (x100)
    """
    return rel_frequence(values, multiplier=100.0)


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
        IndexError: if values is passed as a empty iterable
    """

    values = sorted(values)
    tam = len(values)
    if tam%2 == 1:
        return values[(tam-1)/2]
    half = tam/2
    return (values[half] + values[half-1]) / 2.0
