
import os


def emit_lines(pattern=None):
    lines = []
    for dir_path, dir_names, file_names in os.walk('/Users/fabio/Estudo/Prog/Python/Real_Python/'):
        for file_name in file_names:
            if file_name.endswith('.py'):
                for line in open(os.path.join(dir_path, file_name)):
                    if pattern in line:
                        lines.append(line)
    return lines


print(emit_lines('generator'))