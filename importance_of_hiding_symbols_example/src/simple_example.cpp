#include "foo.h"
#include "bar_no_export.h"

int main(int argc, char** argv)
{
	CallAllExportedFunctions();
	
	ThisCallEveryNonExported();
	
	return 0;
}