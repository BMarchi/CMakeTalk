CMAKE_MINIMUM_REQUIRED(VERSION 3.19)

PROJECT(SIMPLE_PROGRAM CXX)

set(MODIFIED_SRC "${CMAKE_CURRENT_LIST_DIR}/src/foo_modified.cpp")
set(PYTHON_SCRIPT "${CMAKE_CURRENT_LIST_DIR}/modify_source.py")

add_custom_command(
	OUTPUT "${MODIFIED_SRC}"
	COMMAND python "${PYTHON_SCRIPT}"
	VERBATIM
)

SET(SRCS
	"${MODIFIED_SRC}"
	"${CMAKE_CURRENT_LIST_DIR}/src/simple_example.cpp"
)

SET(HDRS
	"${CMAKE_CURRENT_LIST_DIR}/include/foo.h"
)

add_executable(my_executable "${SRCS}" "${HDRS}")

target_include_directories(my_executable
	PUBLIC
		"${CMAKE_CURRENT_LIST_DIR}/include"
)
