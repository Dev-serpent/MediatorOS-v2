#include <stdio.h>
#include <stdlib.h>

// A very simple printf.
int printf(const char* format, ...) {
    // For now, it does nothing.
    (void)format;
    return 0;
}

void abort(void) {
    // Halt and catch fire
    while(1) {}
}
