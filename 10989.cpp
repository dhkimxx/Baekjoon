//Counting Srot [https://www.cs.miami.edu/home/burt/learning/Csc517.091/workbook/countingsort.html]
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

int main() {
	int N, temp; std::cin >> N;
	int count[10001] = { 0, };
	for (int i = 0; i < N; i++) {
		scanf("%d", &temp);
		count[temp]++;
	}
	for (int i = 1; i < sizeof(count)/4; i++) {
		for (int j = 0; j < count[i]; j++) {
			std::cout << i << "\n";
		}
	}
}

/*
//Counting Srot
#include <iostream>

int main() {
	int N; std::cin >> N;
	int* arr = new int[N];
	int* sorted_arr = new int[N];
	int count[10000] = { 0, };
	for (int i = 0; i < N; i++) {
		std::cin >> arr[i];
		count[arr[i] - 1]++;
	}
	for (int i = 0; i < 10000 - 1; i++) {
		count[i + 1] = count[i] + count[i + 1];
	}
	for (int i = N - 1; i > -1; i--) {
		sorted_arr[count[arr[i] - 1] -1] = arr[i];
		count[arr[i] - 1]--;
	}
	for (int i = 0; i < N; i++) {
		std::cout << sorted_arr[i];
	}
}*/