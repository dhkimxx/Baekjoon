#include <iostream>
#include <string>

int main() {
	std::string alphabet[8];
	std::string word;
	std::string space[2];
	int count;

	alphabet[0] = "c=";
	alphabet[1] = "c-";
	alphabet[2] = "dz=";
	alphabet[3] = "d-";
	alphabet[4] = "lj";
	alphabet[5] = "nj";
	alphabet[6] = "s=";
	alphabet[7] = "z=";
	space[0] = "  ";
	space[1] = "   ";

	std::cin >> word;

	count = word.length();
	
	for (int i = 0; i < 8; i++) {
		if (word.find(alphabet[i]) != std::string::npos) {
			word.replace(word.find(alphabet[i]), alphabet[i].length(),space[alphabet[i].length() - 2]);
			count -= alphabet[i].length() - 1;
			i = -1;
		}
	}
	

	std::cout << count;
	return 0;

}