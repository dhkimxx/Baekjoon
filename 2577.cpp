#include <iostream>

int main() {
	int A, B, C, mux, fig[10] = { 0 };
	std::cin >> A >> B >> C;
	mux = A * B * C;

	while (mux != 0) {
		fig[mux % 10]++;
		mux /= 10;
	}
	int j;
	for (j = 0; j < 10; j++) {
		std::cout << fig[j] << "\n";
	}
	return 0;
}