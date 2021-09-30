/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  09/24/2021 15:22:57
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
	ifstream f("test.txt");
	// test.txt
	// hello world\nhave a nice day
	string content;
	string tmp;
	while(1) {
		f >> tmp;
		if (f.eof()) break;
		content += tmp;
	}
	cout << content << endl;
	// above method I will discard symbols like space and \n
	
	f.clear();
	f.seekg(0);
	stringstream buffer;
	buffer << f.rdbuf();
	cout << buffer.str() << endl;
	// above method II is clean and beautiful
	f.close();
	return 0;
}

