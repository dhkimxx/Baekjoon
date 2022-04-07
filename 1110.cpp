#include <iostream>

int main() {
	int in, out,first, second,count=0;

	std::cin >> first;

	if (first < 10)
		first *= 10;

	in = first;
	second = 0;

	do{
		out = in / 10 + in % 10;
		second = (in % 10) * 10 + out % 10;
		in = second;
		count++;
	} while (first != second);

	std::cout << count;
	return 0;
}