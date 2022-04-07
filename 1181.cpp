#include <iostream>
#include <algorithm>

int compare(std::string a, std::string b) {
	if (a.length() == b.length())return a < b;
	return a.length() < b.length();
}

int main() {
	int N; std::cin >> N;
	std::string* arr = new std::string[N];
	for (int i = 0; i < N; i++) {
		std::cin >> arr[i];
		for (int j = 0; j < i; j++) {
			if (arr[j] == arr[i]) {
				i--;
				N--;
			}
		}
	}
	std::sort(arr, arr + N, compare);
	for (int i = 0; i < N; i++) {
		std::cout << arr[i] << "\n";
	}
}