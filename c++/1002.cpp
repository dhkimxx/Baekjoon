#include <iostream>

int main() {
	int tastcase;
	std::cin >> tastcase;
	for (int i = 1; i <= tastcase; i++) {
		int x1, y1, r1, x2, y2, r2, R_square;
		std::cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		R_square = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
		if (x1 == x2 && y1 == y2 && r1 == r2) {
			std::cout << -1 << "\n";
			continue;
		}
		else if ((x1 == x2 && y1 == y2) || (R_square > (r1 + r2) * (r1 + r2)) || (R_square < (r1 - r2) * (r1 - r2))){
			std::cout << 0 << "\n";
			continue;
		}
		else if ((R_square == (r1 + r2) * (r1 + r2)) || (R_square == (r1 - r2) * (r1 - r2))) {
			std::cout << 1 << "\n";
			continue;
		}
		else {
			std::cout << 2 << "\n";
		}
	}
	return 0;
}