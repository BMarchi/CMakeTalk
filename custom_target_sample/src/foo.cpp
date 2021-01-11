#include "foo.h"

void SayHelloWorld()
{
	// Bad namespace
	stlll::cout << "Foo.cpp is saying: Hello World.\n";
	stlll::cout << "Python modified this to make it work.";
}