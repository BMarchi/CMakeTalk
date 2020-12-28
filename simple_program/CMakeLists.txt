# CMake forces you to specify a minimum version.
# Different versions of CMake behave differently, therefore we could
# want to force someone to use a newer version.
CMAKE_MINIMUM_REQUIRED(VERSION 3.19)

# Also we need to specifiy a project's name.
# CXX means that the project is a C++ project. This helps CMake
# identify which compiler to use for unknown extensions (like .cc, which google uses).
PROJECT(SIMPLE_PROGRAM CXX)

# This will be a list of strings.
# CMAKE_CURRENT_LIST_DIR is a variable that it's created by CMake when it runs.
# This expands to the current directory where the CMakeLists.txt is.
# There are other variables that we will use in other examples, but I strongly
# suggest (since I can't force you) to use them instead of hard-coded paths so
# anyone can build your library/executable.
SET(SRCS
	"${CMAKE_CURRENT_LIST_DIR}/src/foo.cpp"
	"${CMAKE_CURRENT_LIST_DIR}/src/simple_example.cpp"
)

SET(HDRS
	"${CMAKE_CURRENT_LIST_DIR}/include/foo.h"
)

add_executable(my_executable "${SRCS}" "${HDRS}")

# Almost everything in CMake is a "target" (libraries & executables, we also have "custom targets").
# This directive is the same as passing the -I flag to the compiler.
target_include_directories(my_executable
	PUBLIC
		"${CMAKE_CURRENT_LIST_DIR}/include"
)

# The equivalent by using command line for Windows is the following:
# cl /Femy_executable.exe src\simple_example.cpp src\foo.cpp /I include

# /Fe<name> is the name of the executable.
# Then we follow the command by the source files.
# /I is the same as target_include_directories
