#include <iostream>
#include <string>
using namespace std;

int main() {
	string str = "first sentence\nsecond sentence\n";	
	int start = 0;
	int end = str.find('\n', start);
	cout << str.substr(start, end-start)<<endl;
	end++;
	start = end;
	end = str.find('\n', start);
	cout << str.substr(start, end-start) << endl;

	start = str.find("second");
	cout << str.substr(start, 6) << endl;
	return 0;
}
