#include <iostream>

int main() {
	int N,i,j;
	
	std::cin >> N;
	for (i = 1; i <= N; i++) {

		for (j = 1; j <= N - i; j++) {
			std::cout << " ";
		}
		for (j = 1; j <= i; j++) {
			std::cout << "*";
		}

		std::cout << "\n";
		
	}
	return 0;
}