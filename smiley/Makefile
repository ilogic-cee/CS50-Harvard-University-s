colorize: colorize.o helpers.o
	clang -o colorize colorize.o helpers.o -I.

colorize.o: colorize.c bmp.h helpers.h
	clang -c colorize.c -o colorize.o -I.

helpers.o: helpers.c bmp.h helpers.h
	clang -c helpers.c -o helpers.o -I.

clean:
	rm -f colorize colorize.o helpers.o
