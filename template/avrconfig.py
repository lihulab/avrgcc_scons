import os

# target name
MCU = 'atmega16'
TARGET_NAME = 'template'

# toolchains options
PLATFORM = 'gcc'
EXEC_PATH = 'H:/Atmel/WinAVR-20100110/bin'

PREFIX = 'avr-'
CC = PREFIX + 'gcc'
AS = PREFIX + 'gcc'
AR = PREFIX + 'ar'
LINK = PREFIX + 'gcc'
TARGET_EXT = 'elf'
SIZE = PREFIX + 'size'
OBJDUMP = PREFIX + 'objdump'
OBJCOPY = PREFIX + 'objcopy'

TARGET = TARGET_NAME + '.' + TARGET_EXT

DEVICE = '-mmcu=' + MCU
CFLAGS = DEVICE
AFLAGS = '-c' + DEVICE
LFLAGS = DEVICE + ' -Wl,--gc-sections,-Map=' + TARGET_NAME + '.map,-cref '

HEXFILE = TARGET_NAME + '.hex'
POST_ACTION = OBJCOPY + ' -O ihex $TARGET ' + HEXFILE
