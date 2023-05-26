#include <iostream>
#include <string>

int main() {
	std::string a, b;
	int length;
	std::cin >> a >> b;


	if (a.length() > b.length())
		length = a.length();
	else
		length = b.length();

	int* A = new int[length];
	int* B = new int[length];
	int* C = new int[length + 1];
	int* ans = new int[length + 1];

	for (int i = 0; i < length; i++) {
		A[i] = int(a[length - i - 1]) - 48;
		B[i] = int(b[length - i - 1]) - 48;
	}
	
	for (int i = 0; i < length; i++) {
		C[i] = 0;
	}
	for (int i = 0; i < length; i++) {
		ans[i] = (A[i] + B[i] + C[i]) % 10;
		if ((A[i] + B[i] + C[i]) >= 10) {
			C[i + 1]++;
			if (i == length - 1) {
				ans[length] = 1;
			}
		}
	}
	for (int i = length; i >= 0; i--) {
		if (i == length) {
			if (ans[i] == 0)
				continue;
		}
		std::cout << ans[i];
	}
}