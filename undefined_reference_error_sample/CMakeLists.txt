CMAKE_MINIMUM_REQUIRED(VERSION 3.19)

PROJECT(add_library_example CXX)

# This function will look for a CMakeLists in the my_library directory that it's defined
# in this dir.
add_subdirectory(my_library)

SET(SRCS
	"${CMAKE_CURRENT_LIST_DIR}/src/foo.cpp"
	"${CMAKE_CURRENT_LIST_DIR}/src/simple_example.cpp"
)

SET(HDRS
	"${CMAKE_CURRENT_LIST_DIR}/include/foo.h"
)

add_executable(my_executable "${SRCS}" "${HDRS}")

target_link_libraries(my_executable PRIVATE my_library)

target_include_directories(my_executable
	PUBLIC
		"${CMAKE_CURRENT_LIST_DIR}/include"
)
