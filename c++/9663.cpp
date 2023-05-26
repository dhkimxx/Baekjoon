#include <iostream>
using namespace std;

int N;
int vx[15 + 1], vy[15 + 1];

int go(int x,int y) {
	for (int i = 0; i < x; i++) {
		if (x == vx[i]) return 0;
		if (y == vy[i]) return 0;
		if (abs(x - vx[i]) == abs(y - vy[i])) return 0;
	}

	if (x == N - 1) {
		return 1;
	}
	vx[x] = x, vy[x] = y;

	int r = 0;
	for (int i = 0; i < N; i++) {
		r += go(x + 1, i);
	}
	return r;
}

int main() {
	cin >> N;
	int r = 0;
	for (int i = 0; i < N; i++) r += go(0, i);
	cout << r;
}
