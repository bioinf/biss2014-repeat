__author__ = 'nikita_kartashov'

from itertools import groupby

from repeat import repeat_class_family, pers_div, left_in_repeat_consensus, matching_repeat, position_in_repeat_start
from utils import sort_data, filterer_by


def group_by_parameter(aggregate_function, data):
    """
    Returns dictionary with grouped data
    :param aggregate_function: function providing key parameter
    :param data: data to group
    :return: grouped data
    """
    def instantiate_list(group_tuple):
        k, v = group_tuple
        return k, list(v)
    return dict(map(instantiate_list, groupby(sort_data(aggregate_function, data), key=aggregate_function)))


def cluster_data(aggregate_function, data, domain_min, domain_max, number_of_clusters):
    """
    Clusters data into given number of pieces
    :param aggregate_function: function aggregating a data item
    :param data: data tuples
    :param domain_min: min value of parameter
    :param domain_max: max value of parameter
    :param number_of_clusters: number of resulting blocks
    :return: the resulting clustered tuples
    """
    domain_width = domain_max - domain_min
    cluster_width = domain_width * 1.0 / number_of_clusters

    def cluster_index(item):
        return int(aggregate_function(item) // cluster_width)
    result = [[] for i in xrange(number_of_clusters)]
    for item in data:
        if aggregate_function(item) <= domain_min or aggregate_function(item) >= domain_max:
            continue
        index = cluster_index(item)
        result[index].append(item)
    return result


def filter_fully_matching(data):
    """
    Leaves only repeats that fully match
    :param data: repeats iterable
    :return: filtered iterable
    """
    return filter(filterer_by(position_in_repeat_start, 1), filter(filterer_by(left_in_repeat_consensus, 0), data))


def group_by_repeat_family(data):
    """
    Groups the repeats by family
    :param data: repeats iterable
    :return: grouped repeats
    """
    return group_by_parameter(repeat_class_family, data)


def group_by_matching_repeat(data):
    """
    Groups the repeats by matching repeat
    :param data: repeats iterable
    :return: grouped repeats
    """
    return group_by_parameter(matching_repeat, data)


def cluster_by_divergence(data, div_min, div_max, number_of_clusters):
    """
    Clusters data by divergence for plotting
    :param data: repeat iterable
    :param div_min: min divergence
    :param div_max: max divergence
    :param number_of_clusters: number of resulting clusters
    :return: clustered items
    """
    return cluster_data(pers_div, data, div_min, div_max, number_of_clusters)


def items_in_clusters(clusters):
    """
    Maps the clusters to the number of items in them
    :param clusters: clusters with data
    :return: list of cluster sizes
    """
    return map(len, clusters)


def items_in_values(dictionary):
    """
    Maps the clustered data in dictionary to the number of items in them
    :param dictionary: clustered dictionary
    :return: list of cluster sizes
    """
    return {key:len(value) for key, value in dictionary.iteritems()}