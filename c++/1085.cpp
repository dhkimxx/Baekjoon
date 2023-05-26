#include <iostream>

int main() {
	int x, y, w, h, xmin, ymin, min;

	std::cin >> x >> y >> w >> h;

	if (w - x > x) {
		xmin = x;
	}
	else {
		xmin = w - x;
	}
	if (h - y > y) {
		ymin = y;
	}
	else {
		ymin = h - y;
	}
	if (xmin > ymin) {
		min = ymin;
	}
	else {
		min = xmin;
	}

	std::cout << min;


}