__author__ = 'nikita_kartashov'

from repeat import sw_score, repeat_class_family, matching_repeat, make_file_repr, split_repeat_line


CHEETAH_DATA_FILE = '/Users/nikita_kartashov/Downloads/cheetah_scaffolds.fa.out'


def sort_data(function, iterable):
    return sorted(iterable, key=function)


def output_data_file_sorted(filename, parameter_name, function, iterable):
    sorted_iterable = sort_data(function, iterable)
    output_to_file(filename + '_' + parameter_name, iterable)
    return sorted_iterable


def output_to_file(filename, data):
    with open(filename, 'w') as outfile:
        outfile.writelines(map(make_file_repr, data))


def get_all_data(file_path, open_mode='r'):
    with open(file_path, open_mode) as input_file:
        return input_file.readlines()


def skip_annotations(lines):
    return lines[3:]


def get_clean_data():
    return map(split_repeat_line, skip_annotations(get_all_data(CHEETAH_DATA_FILE)))


def filterer_by(function, value):
    def real_filter(data):
        return function(data) == value

    return real_filter


def perform_sorting_by_family():
    data_file_lines = get_all_data(CHEETAH_DATA_FILE)
    data_tuples = map(split_repeat_line, skip_annotations(data_file_lines))
    return output_data_file_sorted(CHEETAH_DATA_FILE, 'repeat_class', repeat_class_family, data_tuples)


if __name__ == '__main__':
    perform_sorting_by_family()