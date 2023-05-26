#include <iostream>

char printStar(int i, int j, int n) {
	if (i > n || j > n) {
		i = i % n;
		j = j % n;
	}
	if ((n / 3 <= i) && (i < n * 2 / 3) && (n / 3 <= j) && (j < n * 2 / 3)) {
		return ' ';
	}
	else{
		if (n == 3)
			return '*';
		else
			return printStar(i, j, n / 3);
	}
}

int main() {
	int n = 0;
	std::cin >> n;
	char** star = new  char*[n];
	for (int i = 0; i < n; i++) {
		star[i] = new char[n];
	}


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			star[i][j] = printStar(i, j, n);
			std::cout << star[i][j];
		}
		std::cout << "\n";
	}
	delete[] star;
	return 0;
}