#include <stdint.h>

// options to control how MicroPython is built

#define MICROPY_ENABLE_COMPILER     (1)
#define MICROPY_ENABLE_GC           (1)
#define MICROPY_HELPER_REPL         (1)

// Disable all optional sys module features.
#define MICROPY_PY_SYS_MODULES      (0)

#define MICROPY_USE_INTERNAL_LIBC (1)

// type definitions for the specific machine

typedef long mp_off_t;

// We need to provide a declaration/definition of alloca()
// #include <alloca.h>

#define MICROPY_HW_BOARD_NAME "MediatorOS"
#define MICROPY_HW_MCU_NAME "i686"
#define MICROPY_HEAP_SIZE      (8192) // heap size 8 kilobytes

#define MP_STATE_PORT MP_STATE_VM

// HAL declarations
int mp_hal_stdin_rx_chr(void);
void mp_hal_stdout_tx_strn(const char *str, mp_uint_t len);
