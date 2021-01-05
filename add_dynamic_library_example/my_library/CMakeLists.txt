SET(MY_LIBRARY_SRCS
	"${CMAKE_CURRENT_LIST_DIR}/src/bar.cpp"
)

SET(MY_LIBRARY_HDRS
	"${CMAKE_CURRENT_LIST_DIR}/include/bar.h"
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

# If you run DUMPBIN /EXPORTS my_library.dll
# you'll see something like the following.

# Dump of file my_library.dll

# File Type: DLL

  # Section contains the following exports for my_library.dll

    # 00000000 characteristics
    # FFFFFFFF time date stamp
        # 0.00 version
           # 1 ordinal base
           # 1 number of functions
           # 1 number of names

    # ordinal hint RVA      name

          # 1    0 00001023 ?CallBarPrint@@YAXXZ = @ILT+30(?CallBarPrint@@YAXXZ)

  # Summary

        # 1000 .00cfg
        # 1000 .data
        # 2000 .idata
        # 1000 .pdata
        # 3000 .rdata
        # 1000 .reloc
        # 1000 .rsrc
        # 8000 .text
		

# You can clearly see that the function "CallBarPrint" is exported while the other function it's not.
# It's strongly suggested to not export symbols that are not required for public users (besides, Windows has a 65k symbol limit).
