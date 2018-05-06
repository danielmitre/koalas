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

    >>> mode([1, "mother", "mother", 3, 3])
    set(['mother', 3])

    Args:
        values (iterable): the values that you want the mode
    Returns:
        a set with the values that appears the most
    """
    mapa = {}
    maior = 0
    for v in values:
        if v in mapa:
            mapa[v] += 1
        else:
            mapa[v] = 0

        maior = max(maior, mapa[v])

    res = set()
    for v in mapa:
        if mapa[v] == maior:
            res.add(v)

    return res
