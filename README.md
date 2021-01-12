
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

You can expand variables by either `${my_var}` or `"${my_var}"`. [this guy explains all the different behaviors](https://stackoverflow.com/questions/35847655/when-should-i-quote-cmake-variables). I strongly suggest using the latter version with quotes and the usage of VERBATIM for commands.

## Common functions

There are too many functions already implemented by CMake but I'll name the common ones and how to use them.

### Setting a variable

To create variables in CMake (or modifiy an already existing one), we use the function called `set(<variable_name> <value>)`. Variables are created in the current scope and can be accessed or written from child scopes. To override a value in a child scope, we have to use `set(<variable_name> <value> PARENT_SCOPE)`. This trick can be used for functions to modify variables outside the scope of the function.

### Creating options

We can specify CMake's configuration/build by using **options**. These can be declared using the `set` function like the following

```
set(MY_STRING_OPTION "DefaultValue" CACHE STRING "This variable does some magic stuff!")
set(MY_BOOL_OPTION ON CACHE BOOL "This boolean will show something special")
set(MY_PATH_TO_SOMETHING_GLORIOUS "." CACHE PATH "Use this type when referencing a file somewhere instead of a string!")
```

Then you can change the value of this variable by running:

```
cmake -DMY_BOOL_OPTION=OFF -DMY_STRING_OPTION="I hate default values for strings" -DMY_PATH_TO_SOMETHING_GLORIOUS="/" ../
```

### Globbing

If we have a project with thousand of files, instead of listing each one, we can use `file(GLOB <output_var_name> <path_we_want_to_glob>/*.cpp)`. This will get all cpp files in the given directory and store them in `<output_var_name>`. The downside of this is that if we add new source files, CMake **won't detect them**. We will need to clear the cache and run everything again. It's not recommended to use this for source files.
There are more parameters that can be used with file, like removing or creating directories. You can see more (in the official documentation)[https://cmake.org/cmake/help/latest/command/file.html].

### Execute Process & Custom Command

To run things like python scripts, shell scripts or anything outside CMake (for example, protobuff to generate messages and use that in the compilation of other libraries) exists two functions called `execute_process` and `add_custom_command`. The former works on the *compilation phase* and the latter on the *build phase*.

```
execute_process(
  COMMAND <path_to_my_script>
  RESULT_VARIABLE <my_variable>
)

add_custom_command(
  COMMAND <path_to_my_script>
  OUTPUT <my_variable>
)
```
There are multiple parameters to pass to these functions that can be checked out on the official documentation. If we run execute_process, this will call the script in the *compilation phase* and will wait until it finishes. The custom command will run **if and only if** a *target* depends on the output or if we set the **POST BUILD** argument (not so recommended). You can trick the "always run custom command" by using `add_custom_target` which depends on this custom command.

# CMake Phases

Something to have always on mind are the phases that CMake goes through. We have the *configuration phase* (when we just simply run `cmake <path_to_root_CMakeLists>`) then the *build phase* (`cmake --build <path_to_build>`) and finally the *installation phase* (`cmake --install <path_of_build>`).

## Configuration Phase

As the name implies, this phase goes through all the CMakeLists sequentially and in the order they are declared (subsequents `add_subdirectory` and similars) and creates all the targets found (they **DON'T GET BUILD YET**). In this phase CMake will find syntax errors, missing files and so on.

## Build Phase

CMake will start compiling, running (custom commands for example) and linking all the targets declared in the order it can (meaning independent targets will come first and then targets that depend on these targets).

## Installation phase

In this last phase CMake will *normally* copy and/or move around files for distribution. See `INSTALL(` functions to see how it works.

# TODOs for the reader since I really don't have time to cover everything (i don't know everything either)

* How to install targets
* [Generators](https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html)
* Extending common functions
* And many, many more functionality.


# Author

Brian Marchi
