#include "../include/print.h"
#include <iostream>
void print_large() {
	std::cout << "from print_large: ";
	print_hello_world();
	print_hello_world();
}
