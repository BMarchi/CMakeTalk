CMAKE_MINIMUM_REQUIRED(VERSION 3.19)

PROJECT(using_gtest CXX)

# Required to use FetchContent function
include(FetchContent)

# Declares a package called googletest.
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        master
)

# Download the project (this doesn't check if it was downloaded already).
FetchContent_Populate(googletest)
add_subdirectory(${googletest_SOURCE_DIR})

# From now on, we can use any target from google test.
add_executable(fooTest "${CMAKE_CURRENT_LIST_DIR}/src/foo_test.cpp")

target_link_libraries(fooTest PRIVATE gtest)

target_include_directories(fooTest
	PUBLIC
		"${googletest_SOURCE_DIR}/include"
)
