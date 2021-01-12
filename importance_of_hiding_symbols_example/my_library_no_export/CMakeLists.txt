SET(MY_LIBRARY_SRCS
	"${CMAKE_CURRENT_LIST_DIR}/src/bar_no_export.cpp"
)

SET(MY_LIBRARY_HDRS
	"${CMAKE_CURRENT_LIST_DIR}/include/bar_no_export.h"
)

# add our library as dynamic (dll for windows, so for linux, dylib for OSX).
add_library(my_library_no_export SHARED "${MY_LIBRARY_SRCS}" "${MY_LIBRARY_HDRS}")

target_include_directories(my_library_no_export
	PUBLIC
		"${CMAKE_CURRENT_LIST_DIR}/include"
)

target_compile_definitions(my_library_no_export
	PRIVATE
		-DBAR_COMPILING # This defines the macro necessary to export the symbols when compiling.
)
