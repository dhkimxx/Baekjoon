#include <iostream>
#include <string>

int main() {	
	std::string S;
	int idx;
	std::cin >> S;

	for (char i = 'a'; i <= 'z'; i++) {
		for (int j = 0; j < S.length() + 1; j++) {
			if (S[j] == i) {
				idx = j;
				break;
			}
			idx = -1;
		}
		std::cout << idx << " ";
	}
	return 0;
}