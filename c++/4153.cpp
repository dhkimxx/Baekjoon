#include <iostream>

int main() {
	bool flag = true;
	while (flag) {
		int a[3];
		int max = 0, max_idx = 0, square_sum = 0;
		for (int i = 0; i < 3; i++) {
			std::cin >> a[i];
			if (a[i] > max) {
				max = a[i];
				max_idx = i;
			}
		}		
		if ((a[0] + a[1] + a[2]) == 0)
			break;
		for (int i = 0; i < 3; i++) {
			if (i == max_idx)
				continue;
			square_sum += a[i]*a[i];
		}
		if (max*max == square_sum)
			std::cout << "right" << "\n";
		else
			std::cout << "wrong" << "\n";
	}
	return 0;
}