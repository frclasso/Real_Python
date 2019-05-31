
import os

def generate_filenames():
    """
    Generate a sequence of opened files
    matching a specific extension
    """
    for dir_path, dir_names, file_names in os.walk('../'):
        for file_name in file_names:
            if file_name.endswith('.py'):
                yield open(os.path.join(dir_path, file_name))


def cat_files(files):
    """takes in an iterable if filenames"""
    for fname in files:
        for line in fname:
            yield line


def grep_files(lines, pattern=None):
    """takes in an iterable of line"""
    for line in lines:
        if pattern in line:
            yield line


py_files = generate_filenames()
py_files = cat_files(py_files)
lines = grep_files(py_files, 'countdown')
for lines in lines:
    print(lines)