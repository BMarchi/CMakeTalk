
# CMakeTalk

This repository contains a set of examples to understand how a basic part of CMake works. I decided to use the latest version of CMake at the moment of writing these examples just because I can.

## Requirements to run examples

* CMake 3.19.2

## How to run them

Every example can be run by just going to the build folder, and run in any terminal
`cmake ../
`cmake --build .`

# Glossary

This glossary will cover some of the functionality of CMake with examples and explanations that weren't covered by the samples.

## Defined variables

When CMake starts running, it defines quite a few variables that we can use to reference directories and such.

`CMAKE_CURRENT_LIST_DIR`

This variable expands to the path of the current **CMakeLists** that it's being executed or any **.cmake**.

`CMAKE_CURRENT_SOURCE_DIR`

Better explained by this [answer](https://stackoverflow.com/questions/15662497/difference-between-cmake-current-source-dir-and-cmake-current-list-dir)

`CMAKE_CURRENT_BINARY_DIR`

Binary directory that it's being used by CMake to process binaries (like executables).

`WIN32`

Defined when we are compiling for Windows (either x86 or x64).

`UNIX`

Defined when we are compiling for any Unix-like platform (this includes OSX. For cross-platform you could use 

`APPLE`

Defined when compiling for any platform from Apple (iOS, macOS, tvOS)

The variables to detect to which platform we are building, can be used like the following

```
if(WIN32)
  message(STATUS "Here we can do specific logic for Windows, like compiler flags")
elseif(UNIX AND NOT APPLE)
  message(STATUS "Here we can do specific logic for Linux, like compiler flags")
elseif(APPLE)
  message(STATUS "Here we can do specific logic for Apple, like compiler flags")
else()
  message(STATUS "You can do nothing or stop the process if not supported.")
endif()
```

---------------------------------
You can see the complete list of variables defined [enter link description here](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html)

## Functions

In CMake we can define functions like programming languages. They support **named arguments** and **optional arguments**. We can create them like:

```
function(<name>  [<arg1>  ...])
  <commands>
endfunction()
```

A complete example for a function with named arguments and optional arguments looks like the following:

```
function(my_great_function named_param_one named_param_two)
  message(STATUS "User called 'my_great_function' with param "${named_param_one}" and "${named_param_two}")
  message(STATUS "He also supplied "${ARGN}" optional arguments.")
  foreach(optional_arg IN LISTS ARGN)
        message("Optional Argument: "${optional_arg}" ")
  endforeach()
endfunction()

my_great_function("Hello" "World" ":)")
```
Something important to remember are the defined variables for accessing the arguments. These are

```
ARGC : Total number of arguments(named arguments + optional arguments)
ARGV : list of variables containing both named and optional arguments
ARGN : list of variables containing only optional arguments
```

You can also access the parameters by using `"${ARGV#}"` where # can be changed by any number. If we try to access a variable that does not exists, the behavior is undefined.
Another relevant thing is that functions **do not have return values and also do not modify the given variables.**

## Macros

Macros work almost the same as functions, with the difference that the variables passed to the arguments are modified (you can think them as a C/C++ macro)


```
macro(my_great_macro my_variable_to_modify)
  message(STATUS "Value of my_variable_to_modify: "${my_variable_to_modify}"")
  set(my_variable_to_modify "abc")
endmacro()

set(my_variable_to_modify "ABC")
my_great_macro("${my_variable_to_modify}")
# Here my_variable_to_modify will have the value changed to "abc"
```

## Variable expansion

You can expand variables by either `${my_var}` or `"${my_var}"`. (this guy explains all the different behaviors)[https://stackoverflow.com/questions/35847655/when-should-i-quote-cmake-variables]. I strongly suggest using the latter version with quotes and the usage of VERBATIM for commands.

## Common functions

## Author

Brian Marchi
