#include <iostream>
#include <string>

int main() {
	int n, i, j, count = 0, score = 0;
	std::string ox;
	std::cin >> n;
	for (i = 1; i <= n; i++) {
		std::cin >> ox;
		for (j = 0; j < ox.size(); j++) {
			if (ox[j] == 'O') {
				count++;
				score += count;
			}
			else
				count = 0;
		}
		std::cout << score << "\n";
		score = 0;
		count = 0;
	}
	return 0;
}