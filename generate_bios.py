import os

def generate_bios_header():
    bios_screen = [
        "AMIBIOS(C) 2026 American Megatrends, Inc.",
        "MediatorOS BIOS v0.1",
        "",
        "Main  Advanced  Security  Boot  Exit",
        "",
        "+------------------------------------------------------------------------------+",
        "| System Time: 00:00:00                                                        |",
        "| System Date: 01/31/2026                                                      |",
        "|                                                                              |",
        "| CPU: QEMU Virtual CPU version 2.5+ @ 2.0GHz                                  |",
        "| Memory: 640K Base Memory, 1023M Extended                                     |",
        "|                                                                              |",
        "| Boot Device: CD/DVD                                                          |",
        "|                                                                              |",
        "| Python Interpreter: Enabled                                                  |",
        "|                                                                              |",
        "|                                                                              |",
        "| F10: Save and Exit                                                           |",
        "+------------------------------------------------------------------------------+",
        "",
        "Press any key to continue..."
    ]

    c_string_lines = []
    for line in bios_screen:
        c_string_lines.append('"' + line.replace('"', '\"') + '\n"')

    c_string = "\n".join(c_string_lines)

    header_content = "#ifndef BIOS_SCREEN_H\n"
    header_content += "#define BIOS_SCREEN_H\n\n"
    header_content += "const char* bios_screen_content =\n"
    header_content += c_string + ";\n\n"
    header_content += "#endif // BIOS_SCREEN_H\n"


    # Place the header file inside the kernel directory
    kernel_dir = "mediator/kernel"
    if not os.path.exists(kernel_dir):
        os.makedirs(kernel_dir)

    with open(os.path.join(kernel_dir, "bios_screen.h"), "w") as f:
        f.write(header_content)

if __name__ == "__main__":
    generate_bios_header()
    print("Generated mediator/kernel/bios_screen.h")