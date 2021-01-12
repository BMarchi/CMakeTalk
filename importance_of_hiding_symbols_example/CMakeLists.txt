CMAKE_MINIMUM_REQUIRED(VERSION 3.19)

PROJECT(add_library_example CXX)

# Windows needs to have the dll with the executable in the same directory
# to work. Otherwise, it will crash and will not find the .dll .
if(WIN32)
	set(LIBRARY_OUTPUT_PATH "${CMAKE_BINARY_DIR}")
	set(EXECUTABLE_OUTPUT_PATH "${CMAKE_BINARY_DIR}")
endif()

add_subdirectory(my_library)
add_subdirectory(my_library_no_export)

SET(SRCS
	"${CMAKE_CURRENT_LIST_DIR}/src/foo_exported.cpp"
	"${CMAKE_CURRENT_LIST_DIR}/src/simple_example.cpp"
)

SET(HDRS
	"${CMAKE_CURRENT_LIST_DIR}/include/foo.h"
)

add_executable(my_executable "${SRCS}" "${HDRS}")

target_link_libraries(my_executable PRIVATE my_library my_library_no_export)

target_include_directories(my_executable
	PUBLIC
		"${CMAKE_CURRENT_LIST_DIR}/include"
)
