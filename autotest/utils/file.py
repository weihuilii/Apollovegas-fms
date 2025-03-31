from avfms.utils.file import File
file_path = 'autotest/test_repo/test_file1.txt'

def test():
    file = File(file_path)
    assert file.size == 10000, "Incorrect file size"
    