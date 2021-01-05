#include "foo.h"

#include "bar.h"

void SayHelloWorld()
{
	std::cout << "Foo.cpp is saying: Hello World.\n Next we are going to call Bar Print.\n";
	
	CallBarPrint();
}