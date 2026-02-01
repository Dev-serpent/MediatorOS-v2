
#include <stdio.h>
#include <string.h>

#include "py/compile.h"
#include "py/runtime.h"
#include "py/gc.h"
#include "py/stackctrl.h"

// Defined in linker script
extern uint32_t _heap_start;
extern uint32_t _heap_end;

void kernel_main(void) {
    mp_stack_ctrl_init();
    gc_init(&_heap_start, &_heap_end);
    mp_init();

    pyexec_friendly_repl();

    mp_deinit();
}

void gc_collect(void) {
    gc_collect_start();
    gc_helper_collect_regs_and_stack();
    gc_collect_end();
}
