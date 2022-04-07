#include <iostream>
#include <string>

int main() {
	int N;	std::cin >> N;
	int num = 666, count = 0;
	std::string cmp;
	while (count != N) {
		cmp = std::to_string(num);
		for (int i = 0; i < cmp.length() - 2; i++) {
			if (cmp[i] == '6' && cmp[i + 1] == '6' && cmp[i + 2] == '6') {
				count++;
				break;
			}
		}	
		num++;
	}
	std::cout << cmp;
}