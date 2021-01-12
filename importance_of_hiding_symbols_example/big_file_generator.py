import os
import sys

python_file_path = os.path.dirname(os.path.realpath(__file__))

foo_file_path = os.path.join(python_file_path, "src")
library_with_all_exported = os.path.join(python_file_path, "my_library")
library_with_nothing_exported = os.path.join(python_file_path, "my_library_no_export")

bar_header_file_path_exported = os.path.join(library_with_all_exported, "include", "bar_export.h")
bar_source_file_path_exported = os.path.join(library_with_all_exported, "src", "bar_export.cpp")

bar_header_file_path_non_exported = os.path.join(library_with_nothing_exported, "include", "bar_no_export.h")
bar_source_file_path_non_exported = os.path.join(library_with_nothing_exported, "src", "bar_no_export.cpp")

foo_cpp_using_exported = os.path.join(foo_file_path, "foo_exported.cpp")

bar_header_common_file = """
#pragma once

#if BAR_COMPILING
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT __declspec(dllimport)
#endif  // COMPILING_DLL

"""

bar_source_common_file = """
#include "{}"

#include <iostream>

"""

functions_to_create = 50000

if __name__ == "__main__":
    # Exported
    header_file_full_exported = bar_header_common_file
    header_file_full_exported = header_file_full_exported.format("bar_export.h")
    for i in range(0, functions_to_create):
        header_file_full_exported += "DLL_EXPORT void ExportedFunction{}();\n".format(i)
    with open(bar_header_file_path_exported, "wt") as cpp_file:
        cpp_file.write(header_file_full_exported)
    cpp_source = cpp_source.format("bar_export.h")
    for i in range(0, functions_to_create):
        cpp_source += "void ExportedFunction" + str(i) + "(){ std::cout << \"ExportedFunction " + str(i) + " call\\n\";}\n"
    with open(bar_source_file_path_exported, "wt") as cpp_file:
        cpp_file.write(cpp_source)
    # Non exported
    header_file_non_exported = bar_header_common_file
    header_file_non_exported = header_file_non_exported.format("bar_no_export.h")
    for i in range(0, functions_to_create):
        header_file_non_exported += "void NonExportedFunction{}();\n".format(i)
    header_file_non_exported += "DLL_EXPORT void ThisCallEveryNonExported();"
    with open(bar_header_file_path_non_exported, "wt") as cpp_file:
        cpp_file.write(header_file_non_exported)
    cpp_source = bar_source_common_file
    for i in range(0, functions_to_create):
        cpp_source += "void NonExportedFunction" + str(i) + "(){ std::cout << \"NonExportedFunction " + str(i) + " call\\n\";}\n"
    cpp_source += "void ThisCallEveryNonExported() {\n"
    for i in range(0, functions_to_create):
        cpp_source += "NonExportedFunction{}();\n".format(i)
    cpp_source += "}"
    with open(bar_source_file_path_non_exported, "wt") as cpp_file:
        cpp_file.write(cpp_source)
    
    foo_cpp_complete_file = "#include \"bar_export.h\"\n#include \"foo.h\"\nvoid CallAllExportedFunctions(){\n"
    for i in range(0, functions_to_create):
        foo_cpp_complete_file += "ExportedFunction{}();\n".format(i)
    foo_cpp_complete_file += "}"
    with open(foo_cpp_using_exported, "wt") as cpp_file:
        cpp_file.write(foo_cpp_complete_file)
        
    
    