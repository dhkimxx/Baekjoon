#include <iostream>

int main() {
	int testnum, a, b, i;

	std::cin >> testnum;
	for (i = 0; i < testnum; i++) {
		std::cin >> a >> b;
		std::cout << "Case #" << i + 1 << ": " << a << " + " << b << " = " << a + b << "\n";
	}
	return 0;
}