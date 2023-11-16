# Makefile
CC = clang
CFLAGS = -ggdb3 -O0 -Qunused-arguments -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow

all: colorize

colorize: colorize.c helpers.c bmp.h helpers.h
	$(CC) $(CFLAGS) -o colorize colorize.c helpers.c -lm

clean:
	rm -f *.o a.out core colorize
