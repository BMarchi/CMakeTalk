
# undefined_reference_error_sample

This sample demonstrates a common error that happens during the linking phase.
This will always fail, but you can make it work. The solution is found in the corresponding .cpp file.

# Error

The error you'll see, will depend on the platform. In Windows, we are going to see something like the following:

`foo.obj : error LNK2019: unresolved external symbol "void __cdecl CallBarPrint(void)" (?CallBarPrint@@YAXXZ) referenced in function "void __cdecl SayHelloWorld(void)" (?SayHelloWorld@@YAXXZ) [C:\CMakeTalk\CMakeTalk\undefined_reference_error_sample\build\my_executable.vc
xproj]`

The error is straightforward. This is telling us that the function CallBarPrint that was referenced by SayHelloWorld wasn't found.
This is because the implementation is missing.
