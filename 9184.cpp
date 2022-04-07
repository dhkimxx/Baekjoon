#include<iostream>
using namespace std;

int arr[101][101][101] = { 0 };

int w(int a, int b, int c) {
	int i = a + 50, j = b + 50, k = c + 50;
	if (!arr[i][j][k]) {
		if (a <= 0 || b <= 0 || c <= 0) { 
			return arr[i][j][k] = 1;;
		}
		else if (a > 20 || b > 20 || c > 20) {
			return arr[i][j][k] = w(20, 20, 20);
		}
		else if (a < b && b < c) {
			return arr[i][j][k] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
		}
		else {
			return arr[i][j][k] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
		}
	}
	else
		return arr[i][j][k];
}

int main() {
	int a, b, c, result;
	while (1) {
		cin >> a >> b >> c;
		if (a == -1 && b == -1 && c == -1)
			return 0;
		result = w(a, b, c);
		printf("w(%d, %d, %d) = %d\n", a, b, c, result);
	}
}