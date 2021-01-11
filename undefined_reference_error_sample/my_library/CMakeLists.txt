SET(MY_LIBRARY_SRCS
	"${CMAKE_CURRENT_LIST_DIR}/src/bar.cpp"
)

SET(MY_LIBRARY_HDRS
	"${CMAKE_CURRENT_LIST_DIR}/include/bar.h"
)

add_library(my_library STATIC "${MY_LIBRARY_SRCS}" "${MY_LIBRARY_HDRS}")

target_include_directories(my_library
	PUBLIC
		"${CMAKE_CURRENT_LIST_DIR}/include"
)