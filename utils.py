__author__ = 'nikita_kartashov'

from itertools import groupby


def sort_data(sort_function, iterable):
    """
    Sorts the data using *sort_function*
    :param sort_function: Key function for sorting
    :param iterable: data to sort
    :return: sorted data
    """
    return sorted(iterable, key=sort_function)


def filterer_by(aggregate_function, model_value):
    """
    Returns filtering function, specified by *model_value*
    :param aggregate_function: Function giving the value to compare to
    :param model_value: The value to be compared
    :return: Filtering function
    """
    def real_filter(data):
        return aggregate_function(data) == model_value
    return real_filter