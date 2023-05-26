#include <iostream>
#include <string>

int main() {
	std::string input;
	int num[2];
	char buf;

	for (int i = 0; i < 2; i++) {
		std::cin >> input;
		buf = input[0];
		input[0] = input[2];
		input[2] = buf;
		num[i] = std::stoi(input);
	}
	if (num[0] > num[1])
		std::cout << num[0];
	else
		std::cout << num[1];

	return 0;
}