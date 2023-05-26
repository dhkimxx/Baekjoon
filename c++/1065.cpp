#include <iostream>

int check(int n) {
	int gap, result, buf;
	if (n < 100) {
		result = 1;
		return result;
	}
	if (n == 1000) {
		result = 0;
		return result;
	}

	buf = n % 10;
	n = n / 10;
	gap = buf - n % 10;

	buf = n % 10;
	n = n / 10;

	if (gap == buf - n)
		result = 1;
	else
		result = 0;

	return result;
}

int main() {
	int N, count;;
	count = 0;
	std::cin >> N;
	
	for (int i = 1; i <= N; i++) {
		//std::cout << i << " : " << check(i) << "\n";
		if (check(i) == 1) {
			count++;
		}
	}
	std::cout << count;

	return 0;
}