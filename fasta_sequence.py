__author__ = 'nikita_kartashov'


def read_naive_fasta(filename):
    """
    Naively (in full) reads genome from file in FASTA format
    :param filename file with genome
    :return read genome
    """
    lines = []
    with open(filename, 'r') as input_file:
        while True:
            line = input_file.readline().strip()
            if not line:
                break
            if line.startswith('>'):
                continue
            lines.append(line)
    return ''.join(lines)


class FastaSequence(object):
    """
    NOT YET WORKING
    """
    def __init__(self, file_instance):
        self.__file_instance = file_instance
        self.__parts = []

    def __getitem__(self, index):
        self.ensure_read_to_index(index)
        return self.__get(index)

    def ensure_read_to_index(self, index):
        while self.__max_index() < index:
            self.__read()

    def slice(self, i, j):
        self.ensure_read_to_index(j)
        return ''.join(FastaSequence.__subslice(part, i, j) for part in self.__parts)

    @staticmethod
    def __subslice(part, i, j):
        length = j - i
        if FastaSequence.__part_between(part, i, j):
            return FastaSequence.__part_data(part)
        if FastaSequence.__index_in_part(part, i):
            return FastaSequence.__part_data(part)[i - FastaSequence.__part_start(part):length]
        if FastaSequence.__index_in_part(part, j - 1):
            return FastaSequence.__part_data(part)[:j - FastaSequence.__part_start(part)]
        return ''

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __get(self, index):
        for part in self.__parts:
            if index > FastaSequence.__part_length(part):
                index -= FastaSequence.__part_length(part)
            else:
                return FastaSequence.__part_data(part)[index]

    def __read(self):
        while True:
            line = self.__file_instance.readline().strip()
            if not line:
                return False
            if not line.startswith('>'):
                break

        self.__parts.append((self.__new_part_index(), len(line), line))
        return True

    def __new_part_index(self):
        if not self.__parts:
            return 0
        return self.__max_index() + 1

    def __max_index(self):
        if not self.__parts:
            return 0
        return FastaSequence.__last_index_of_part(self.__parts[::-1][0])

    def close(self):
        self.__file_instance.close()

    @staticmethod
    def __last_index_of_part(part):
        return FastaSequence.__part_start(part) + FastaSequence.__part_length(part) - 1

    @staticmethod
    def __index_in_part(part, index):
        return FastaSequence.__part_start(part) <= index < FastaSequence.__last_index_of_part(part)

    @staticmethod
    def __part_between(part, i, j):
        return FastaSequence.__part_start(part) >= i and FastaSequence.__last_index_of_part(part) <= j

    @staticmethod
    def __part_start(part):
        return part[0]

    @staticmethod
    def __part_length(part):
        return part[1]

    @staticmethod
    def __part_data(part):
        return part[2]

TEST_PATH = '/Users/nikita_kartashov/Downloads/cheetahScaffoldsRmTrf.fa'

if __name__ == '__main__':
    lol = read_naive_fasta(TEST_PATH)
    print('DOne')