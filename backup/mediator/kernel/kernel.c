#include "kernel.h"
#include "bios_screen.h"

volatile unsigned char *video = (unsigned char*)0xb8000;
int cursor_x = 0;
int cursor_y = 0;

void print_char(char c, char color) {
    if (c == '\n') {
        cursor_x = 0;
        cursor_y++;
    } else {
        const int index = (cursor_y * 80 + cursor_x) * 2;
        video[index] = c;
        video[index+1] = color;
        cursor_x++;
        if (cursor_x >= 80) {
            cursor_x = 0;
            cursor_y++;
        }
    }
    // TODO: scrolling
}

void print_string(const char *str) {
    int i = 0;
    while (str[i] != 0) {
        print_char(str[i], 0x07);
        i++;
    }
}

void main() {
    // Clear screen
    for (int i = 0; i < 80 * 25; i++) {
        video[i*2] = ' ';
        video[i*2+1] = 0x07;
    }

    // Print BIOS screen
    print_string(bios_screen_content);

    // Simulate a delay
    for (volatile int i = 0; i < 100000000; i++);

    // Clear screen again
    for (int i = 0; i < 80 * 25; i++) {
        video[i*2] = ' ';
        video[i*2+1] = 0x07;
    }

    cursor_x = 0;
    cursor_y = 0;

    // Start MicroPython
    extern void micropython_main();
    micropython_main();

    return;
}
