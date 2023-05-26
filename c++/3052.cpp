#include <iostream>

int main() {
	int arr[42] = { 0 }, input;
	int i,count=0;

	for (i = 0; i < 10; i++) {
		std::cin >> input;
		if (!arr[input % 42]++)
			count++;
	}
	std::cout << count;
	return 0;
}