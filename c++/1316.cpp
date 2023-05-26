#include <iostream>
#include <string>

int main() {
	int case_n, count = 0;
	char buf;
	std::string word;
	std::string alphabet = "abcdefghijklmnopqrstuvwxyz";

	std::cin >> case_n;
	for (int i = 0; i < case_n; i++) {
		std::cin >> word;

		buf = word[0];
		int arr[26] = { 0, };

		for (int j = 0; j < word.length(); j++) {	
			if (arr[alphabet.find(word[j])] > 0) {
				if (buf != word[j]) {
					count++;
					break;
				}
			}
			else {
				arr[alphabet.find(word[j])] = 1;
			}
			buf = word[j];
		}
	}
	std::cout << case_n - count;
	return 0;
}