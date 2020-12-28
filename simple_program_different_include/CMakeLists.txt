# See simple_program to understand each of these functions.

CMAKE_MINIMUM_REQUIRED(VERSION 3.19)

PROJECT(SIMPLE_PROGRAM CXX)

SET(SRCS
	"${CMAKE_CURRENT_LIST_DIR}/src/foo.cpp"
	"${CMAKE_CURRENT_LIST_DIR}/src/simple_example.cpp"
)

SET(HDRS
	"${CMAKE_CURRENT_LIST_DIR}/include/foo/foo.h"
)

add_executable(my_executable "${SRCS}" "${HDRS}")

# Note that since we changed the directory structure of foo, we either have
# to change the directory here or we need to change the include in each source file.
target_include_directories(my_executable
	PUBLIC
		"${CMAKE_CURRENT_LIST_DIR}/include/foo"
)

# If we want to include the whole "include" directory,
# then for each .cpp file we would need to change the following:
# #include "foo.h" (old include)
# #include "foo/foo.h" (new include)

# The next statement should be used if the above thing is desired
#target_include_directories(my_executable
#	PUBLIC
#		"${CMAKE_CURRENT_LIST_DIR}/include"
#)
