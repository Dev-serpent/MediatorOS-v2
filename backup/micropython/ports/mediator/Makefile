include ../../py/mkenv.mk

# qstr definitions (must come before including py.mk)
QSTR_DEFS = qstrdefsport.h

# MicroPython feature configurations
MICROPY_ROM_TEXT_COMPRESSION ?= 0

# include py core make definitions
include $(TOP)/py/py.mk

CROSS_COMPILE ?= i686-elf-

INC += -I.
INC += -I$(TOP)
INC += -I$(BUILD)
INC += -I../../../../mediator/kernel

CFLAGS += -nostdinc -I$(TOP)/lib/libc
CFLAGS += $(INC) -Wall -Werror -std=c99 -nostdlib -m32 -ffreestanding -O2 -g $(COPT)

# Flags for optional C++ source code
CXXFLAGS += $(filter-out -std=c99,$(CFLAGS))

LIBS =

SRC_C = \
	main.c \
	mphalport.c \
	shared/libc/printf.c \
	shared/readline/readline.c \
	shared/runtime/pyexec.c \
	shared/runtime/stdout_helpers.c

SRC_QSTR += shared/readline/readline.c shared/runtime/pyexec.c

OBJ += $(PY_CORE_O)
OBJ += $(addprefix $(BUILD)/, $(SRC_C:.c=.o))
OBJ += $(addprefix $(BUILD)/, $(SRC_CXX:.cpp=.o))

all: $(BUILD)/libmicropython.a

$(BUILD)/libmicropython.a: $(OBJ)
	$(ECHO) "AR $@"
	$(Q)$(AR) rcs $@ $^

include $(TOP)/py/mkrules.mk
