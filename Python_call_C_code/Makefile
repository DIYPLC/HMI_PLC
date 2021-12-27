all:
	gcc -c -Wall -Werror -fpic ./LibPlc/*.c #Compile: ./LibPlc/*.c -> ./*.o
	gcc -shared -o LibPlc.so *.o            #Linker : ./*.o -> ./*.so
	rm -rf *.o                              #Clean files ./*.o
	python3 __main__.py                     #Run call LibPlc.so
