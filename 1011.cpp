#include <iostream>

int main() {
	long int x, y, testcase, length, count;
	long int sum, n;

	std::cin >> testcase;

	for (int i = 0; i < testcase; i++) {
		std::cin >> x >> y;
		length = y - x;

		count = 0;
		sum = 0;
		n = 0;

		while (1) {

			n++;
			count++;
			if (!(count % 2))
				n--;

			sum += n;
			//std::cout << "count: " << count << " n: " << n << " sum: " << sum << "\n";
			if (sum >= length)
				break;

			
		}
		std::cout << count << "\n";
	}

	return 0;
}