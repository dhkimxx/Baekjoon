#include <iostream>
#include <string>

int main(){
	std::string str;
	int count = 1;

	std::getline(std::cin, str);

	for (int i = 0; i < str.length(); i++) {
		if ((int)str[i] == 32) {
			count++;
		}
	}
	if ((int)str.front() == 32)
		count--;
	if ((int)str.back() == 32)
		count--;

	std::cout << count;
	return 0;
}