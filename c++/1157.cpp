#include <iostream>
#include <string>

int main() {
	std::string word;
	std::string list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	
	int max = 0, idx = 0, overlap_flag = 1;

	std::cin >> word;
	int arr[26] = { 0, };

	for (int i = 0; i < word.length(); i++) {
			if ((int)word[i] >= 97)
				word[i] = (char)((int)word[i] - 32);
	}
	
	for (int i = 0; i < list.length(); i++) {
		for (int j = 0; j < word.length(); j++) {
			if (list[i] == word[j]) {
				arr[i]++;
			}
		}

		if (arr[i] > max) {
			max = arr[i];
			idx = i;
			overlap_flag = 1;
		}
		else if (arr[i] == max) {
			overlap_flag = 0;
		}
	}
	/*
	for (int i = 0; i < 26; i++)
		std::cout << arr[i];

	std::cout << std::endl;
	for (int i = 0; i < 26; i++)
		std::cout << list[i];
		*/

	if (overlap_flag)
		std::cout << list[idx];
	else
		std::cout << "?";

	return 0;
}