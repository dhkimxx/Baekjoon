#include <iostream>
#include <string>

int main() {
	std::string dial[8];
	std::string word;
	int time = 0, count = 0;

	dial[0] = "ABC";
	dial[1] = "DEF";
	dial[2] = "GHI";
	dial[3] = "JKL";
	dial[4] = "MNO";
	dial[5] = "PQRS";
	dial[6] = "TUV";
	dial[7] = "WXYZ";

	std::cin >> word;
	for (int i = 0; i < word.length(); i++) {
		for (int j = 0; j < 8; j++) {
			if (dial[j].find(word[i]) != std::string::npos) {
				time += 3 + j;
			}
		}
	}

	std::cout << time;

	return 0;
}