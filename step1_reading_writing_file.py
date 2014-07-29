__author__ = 'nikita_kartashov'

from repeat import sw_score, repeat_class_family, matching_repeat, make_file_repr, split_repeat_line


def output_to_file(filename, data, repr_func=make_file_repr):
    """
    Outputs all tuples to file using *repr_func*
    :param filename: file to dump the data to
    :param data: iterable of data tuples
    :param repr_func: function returning the string representation of the tuple
    :return:
    """
    with open(filename, 'w') as outfile:
        outfile.writelines(map(repr_func, data))


def get_all_data(filename, open_mode='r'):
    """
    Naively reads all data from *filename* to memory
    :param filename: file with data
    :param open_mode: mode of opening the file
    :return: all lines from file
    """
    with open(filename, open_mode) as input_file:
        return input_file.readlines()


def skip_annotations(lines):
    """
    Returns clean data from a file for processing
    :param lines: lines of the input file
    :return: lines but the first 3 as they are annotations
    """
    return lines[3:]


def get_clean_data(filename):
    """
    Gets all data from
    :param filename file with data
    :return: list of data tuples
    """
    return map(split_repeat_line, skip_annotations(get_all_data(filename)))