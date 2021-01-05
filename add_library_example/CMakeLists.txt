CMAKE_MINIMUM_REQUIRED(VERSION 3.19)

PROJECT(add_library_example CXX)

SET(MY_LIBRARY_SRCS
	"${CMAKE_CURRENT_LIST_DIR}/my_library/src/bar.cpp"
)

SET(MY_LIBRARY_HDRS
	"${CMAKE_CURRENT_LIST_DIR}/my_library/include/bar.h"
)

add_library(my_library STATIC "${MY_LIBRARY_SRCS}" "${MY_LIBRARY_HDRS}")

target_include_directories(my_library
	PUBLIC # By making this public, any other library or executable that uses any of the "my_library" headers can be used without specifiying so.
		"${CMAKE_CURRENT_LIST_DIR}/my_library/include"
)

SET(SRCS
	"${CMAKE_CURRENT_LIST_DIR}/src/foo.cpp"
	"${CMAKE_CURRENT_LIST_DIR}/src/simple_example.cpp"
)

SET(HDRS
	"${CMAKE_CURRENT_LIST_DIR}/include/foo.h"
)

add_executable(my_executable "${SRCS}" "${HDRS}")

# This is the function we have to use to link against created libraries.
# The PRIVATE keyword can be changed to PUBLIC or INTERFACE.
# Private libraries won't be available from any other target that links to this, so it will need
# to link against my library too.
target_link_libraries(my_executable PRIVATE my_library)

target_include_directories(my_executable
	PUBLIC
		"${CMAKE_CURRENT_LIST_DIR}/include"
)

#target_include_directories(my_library
#	PRIVATE # NOTE THE PRIVATE KEYWORD.
#		"${CMAKE_CURRENT_LIST_DIR}/my_library/include"
#)

#target_include_directories(my_executable
#	PUBLIC
#       "${CMAKE_CURRENT_LIST_DIR}/my_library/include" # <= We would need to specify the include here if we make the above include private.
#		"${CMAKE_CURRENT_LIST_DIR}/include"
#)

# To see the symbols created, you can run in a Developer Command Tools (Windows)
# DUMPBIN /SYMBOLS <path_to.lib> /OUT:my_library_symbols.txt
# You can see, besides some STL symbols, the "CallBarPrint" function. 

