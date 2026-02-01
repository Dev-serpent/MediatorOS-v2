#include <unistd.h>
#include "py/mpconfig.h"
#include "kernel.h" // This will be the header for the kernel

// Receive single character
int mp_hal_stdin_rx_chr(void) {
    // For now, there is no keyboard driver, so we just return a character.
    return 'a';
}

// Send string of given length
void mp_hal_stdout_tx_strn(const char *str, mp_uint_t len) {
    // This is a temporary implementation. We'll need to create a proper
    // print_strn function in the kernel.
    char temp[len + 1];
    for (mp_uint_t i = 0; i < len; i++) {
        temp[i] = str[i];
    }
    temp[len] = '\0';
    print_string(temp);
}
