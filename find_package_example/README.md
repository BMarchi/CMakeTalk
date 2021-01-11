
# find_package_example

This demo contains the minimal necessary code to make a "find_package" call to work.
This CMake function is used to add already compiled projects to our workflow.
See [the official documentation](https://cmake.org/cmake/help/latest/command/find_package.html) for more info.

Note that for the find_package to work, we need the "<lib_name>Config.cmake". If that file does not exists, we can't use it.
We would need to set the library using other ways that are not covered in this sample.

# Requirements

Download GTest and compile it.
- git clone https://github.com/google/googletest
- mkdir googletest/build
- mkdir googletest/install_g
- cd googletest/build
- cmake -DCMAKE_BUILD_TYPE="Release" -DCMAKE_INSTALL_PREFIX="../install_g" ../
- cmake --build . --config Release
- cmake --install .

# Building our example

- mkdir build
- cd build
- cmake -DCMAKE_BUILD_TYPE="Release" ../
- cmake --build . --config Release
