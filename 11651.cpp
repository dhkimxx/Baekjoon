#include <iostream>
#include <algorithm>

struct Point
{
	int x, y;
};

int compare(Point a, Point b) {
	if (a.y == b.y) return a.x < b.x;
	return a.y < b.y;
}

int main(void) {
	int N; std::cin >> N;
	Point* p = new Point[N];
	for (int i = 0; i < N; i++) {
		std::cin >> p[i].x >> p[i].y;
	}
	std::sort(p, p + N, compare);
	for (int i = 0; i < N; i++) {
		std::cout << p[i].x << " " << p[i].y << "\n";
	}
}