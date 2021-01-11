import os
import sys

python_file_path = os.path.dirname(os.path.realpath(__file__))
cpp_full_path = os.path.join(python_file_path, "src", "foo.cpp")
cpp_modified_full_path = os.path.join(python_file_path, "src", "foo_modified.cpp")

if __name__ == "__main__":
    if not os.path.isfile(cpp_full_path):
        print("File {} does not exists.".format(cpp_full_path))
        sys.exit(1)
    print("Modifying source file {}".format(cpp_full_path))
    file_data = ''
    with open(cpp_full_path, "rt") as cpp_file:
        file_data = cpp_file.read()
    file_data = file_data.replace('stlll', 'std')
    with open(cpp_modified_full_path, "wt") as cpp_file:
        cpp_file.write(file_data)
    print("Data replaced")
    