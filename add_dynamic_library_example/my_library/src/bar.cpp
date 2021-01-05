#include "bar.h"

#include <iostream>

void NonExportedFunction()
{
	std::cout << "Bar.cpp says Hello World\n";
}

void CallBarPrint()
{
	NonExportedFunction();
}
