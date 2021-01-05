#pragma once

#if BAR_COMPILING
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT __declspec(dllimport)
#endif  // COMPILING_DLL

DLL_EXPORT void CallBarPrint();

void NonExportedFunction();