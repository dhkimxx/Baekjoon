#include <iostream>
#include <string>

int main() {
	int T, R;
	std::string S;
	std::string P = "";
	std::cin >> T;

	for (int i = 1; i <= T; i++) {
		std::cin >> R >> S;
		P = "";
		for (int j = 1; j <= S.length(); j++) {
			for (int k = 1; k <= R; k++) {
				P += S[j - 1];
			}
		}
		std::cout << P << std::endl;
	}
	return 0;
}