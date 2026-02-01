#!/bin/bash
set -e

# Build the OS
make all

# Create a bootable ISO
mkdir -p iso/boot
cp build/kernel.bin iso/boot/kernel.bin
cp -r boot/grub iso/boot/
grub-mkrescue -o mediator.iso iso
