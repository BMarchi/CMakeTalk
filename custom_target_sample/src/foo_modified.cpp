#include "foo.h"

void SayHelloWorld()
{
	// Bad namespace
	std::cout << "Foo.cpp is saying: Hello World.\n";
	std::cout << "Python modified this to make it work.";
}