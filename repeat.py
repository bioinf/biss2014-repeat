__author__ = 'nikita_kartashov'


def split_repeat_line(line):
    return line.split()


def sw_score(data_tuple):
    return int(data_tuple[0])


def pers_div(data_tuple):
    return float(data_tuple[1])


def query_sequence(data_tuple):
    return data_tuple[4]


def query_position_begin(data_tuple):
    return int(data_tuple[5])


def query_position_end(data_tuple):
    return int(data_tuple[6])


def matching_repeat(data_tuple):
    return data_tuple[9]


def repeat_class_family(data_tuple):
    return data_tuple[10]


def position_in_repeat_start(data_tuple):
    return int(data_tuple[11])


def left_in_repeat_consensus(data_tuple):
    return int(data_tuple[13].strip('()'))


def make_file_repr(data_tuple):
    return  ' '.join(data_tuple) + '\n'