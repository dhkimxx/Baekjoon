#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
	int N, temp; std::cin >> N;
	double mean = 0;
	int median = 0, mode = 0, range = 0;
	int max = -4000, min = 4000, max_count = 0;
	int count[8001] = { 0 };
	int mode_arr[8001] = { 0 };
	int* arr = new int[N];

	for (int i = 0; i < N; i++) {
		cin >> temp;
		arr[i] = temp;
		mean += temp;
		count[temp + 4000]++;
		if (max_count < count[temp + 4000]) {
			max_count = count[temp + 4000];
		}
		if (max < temp)
			max = temp;
		if (min > temp)
			min = temp;
	}
    
	for (int i = -4000, k = 0; i < 4001; i++) {
		mode_arr[i + 4000] = 4001;
		if (max_count == count[i + 4000]) {
			mode_arr[k] = i;
			k++;
		}
	}

	sort(mode_arr, mode_arr + 8001);
	if (mode_arr[1] < 4001)
		mode = mode_arr[1];
	else
		mode = mode_arr[0];

	mean = round(mean / N);
    if(mean == -0)
        mean = 0;
	sort(arr, arr + N);
	median = arr[(N - 1) / 2];

	range = max - min;

	cout << mean << "\n" << median << "\n" << mode << "\n" << range;
}
