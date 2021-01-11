CMAKE_MINIMUM_REQUIRED(VERSION 3.19)

PROJECT(using_gtest CXX)

set(OUR_GTEST_PATH_LOCATION "${CMAKE_CURRENT_LIST_DIR}/../googletest/install_g/lib/cmake")

find_package(GTest REQUIRED HINTS "${OUR_GTEST_PATH_LOCATION}")

# This is required since gtest was created by statically linking runtime libraries.
if(MSVC)
    add_compile_options(
        $<$<CONFIG:>:/MT> #---------|
        $<$<CONFIG:Debug>:/MTd> #---|-- Statically link the runtime libraries
        $<$<CONFIG:Release>:/MT> #--|
    )
endif()

# From now on, we can use any target from google test.
add_executable(fooTest "${CMAKE_CURRENT_LIST_DIR}/src/foo_test.cpp")

target_link_libraries(fooTest PRIVATE GTest::gtest)

target_include_directories(fooTest
	PUBLIC
		"${OUR_GTEST_PATH_LOCATION}"
)
