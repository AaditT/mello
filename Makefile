all:
	clang++ -o mello mello.cc algos.cc -std=c++14
clean:
	rm -f mello
