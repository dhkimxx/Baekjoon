#include <iostream>

int HanoiTower(int n, char from, char mid, char to) {

	if (n == 1) {
		std::cout << from << " " << to << "\n";
		return 0;
	}
	HanoiTower(n - 1, from, to, mid);
	std::cout << from << " " << to << "\n";
	HanoiTower(n - 1, mid, from, to);
	return 0;
}


int main() {
	int N;
	int count; std::cin >> N;
	std::cout << (1 << N) - 1 << "\n";
	HanoiTower(N, '1', '2', '3');
}
