from avfms.utils.file import File
file_path = 'autotest/test_repo/test_file1.txt'

def test():

    def _raise_assert_error(key, value):
        assert file.get(key) == value, f'{key} is not correct: current {file.get(key)}, except {value}'

    file = File(file_path)
    _raise_assert_error('file_path', file_path)
    _raise_assert_error('size', 10000)
    _raise_assert_error('directory', 'autotest/test_repo')
    _raise_assert_error('filename', 'test_file1.txt')
    