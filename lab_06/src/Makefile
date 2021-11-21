CFLAGS := -std=c99 -lm
FILE_O := $(subst .c,.o,$(wildcard src/*.c))
HEADERS_DIR := inc/

app.exe:  main.o $(FILE_O)
	gcc -o app.exe $^  $(CFLAGS)


main.o: main.c
	gcc -c -I $(HEADERS_DIR) $^ $(CFLAGS)

src/%.o: src/%.c
	gcc -o $@ -c -I $(HEADERS_DIR) $^ $(CFLAGS)

clean:
	rm -f *.o *.exe src/*.o 

run:
	./app.exe 
