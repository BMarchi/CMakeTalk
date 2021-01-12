SET(MY_LIBRARY_SRCS
	"${CMAKE_CURRENT_LIST_DIR}/src/bar_export.cpp"
)

SET(MY_LIBRARY_HDRS
	"${CMAKE_CURRENT_LIST_DIR}/include/bar_export.h"
)

# add our library as dynamic (dll for windows, so for linux, dylib for OSX).
add_library(my_library SHARED "${MY_LIBRARY_SRCS}" "${MY_LIBRARY_HDRS}")

target_include_directories(my_library
	PUBLIC
		"${CMAKE_CURRENT_LIST_DIR}/include"
)

target_compile_definitions(my_library
	PRIVATE
		-DBAR_COMPILING # This defines the macro necessary to export the symbols when compiling.
)
