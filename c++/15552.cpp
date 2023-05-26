#include <iostream>

int main() {
	std::cin.tie(NULL);
	std::ios::sync_with_stdio(false);

	int i, testnum, a, b;

	std::cin >> testnum;
	for (i = 0; i < testnum; i++)
	{
		std::cin >> a >> b;
		std::cout << a + b << "\n";
	}


}