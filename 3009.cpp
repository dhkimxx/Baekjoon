#include<iostream>

int main() {
	int x[3], y[3], side, max_side = 0;
	double x_center, y_center, x_result, y_result;


	for (int i = 0; i < 3; i++) {
		std::cin >> x[i];
		std::cin >> y[i];
	}

	for (int i = 0; i < 3; i++) {
		for (int j = i + 1; j < 3; j++) {
			side = (x[i] - x[j])* (x[i] - x[j]) + (y[i] - y[j])*(y[i] - y[j]);
			if (max_side <= side) {
				max_side = side;
				x_center = (x[i] + x[j]) / 2.0;
				y_center = (y[i] + y[j]) / 2.0;
				if (i == 0 && j == 1) {
					x_result = x_center * 2 - x[2];
					y_result = y_center * 2 - y[2];
				}
				else if (i == 0 && j == 2) {
					x_result = x_center * 2 - x[1];
					y_result = y_center * 2 - y[1];
				}
				else if (i == 1 && j == 2) {
					x_result = x_center * 2 - x[0];
					y_result = y_center * 2 - y[0];
				}
			}
		}
	}

	std::cout << x_result << " " << y_result;

}