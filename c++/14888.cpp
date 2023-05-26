#include <iostream>
#include <vector>
using namespace std;

vector <int> a, o;
int Max = -1000000000, Min = 1000000000;
int final;

int sum(int n, int result) {
	return result = result + n;
}

int sub(int n, int result) {
	return result = result - n;
}

int mul(int n, int result) {
	return result = result * n;
}

int divv(int n, int result) {
	return result = result / n;
}

int Operator(int N, int result) {
	int result_temp = result;
	if (N == final) {
		if (result > Max)
			Max = result;
		if (result < Min) {
			Min = result;
		}
		return 0;
	}
	for (int i = 0; i < 4; i++) {
		if (o[i] == 0) {
			continue;
		}
		else {
			if (i == 0) {
				result = sum(a[N], result);
			}
			if (i == 1) {
				result = sub(a[N], result);
			}
			if (i == 2) {
				result = mul(a[N], result);
			}
			if (i == 3) {
				result = divv(a[N], result);
			}
			o[i]--;
			Operator(N + 1, result);
			o[i]++;
			result = result_temp;
		}
	}
	return 0;
}

int main() {
	int N; cin >> N;
	final = N - 1;
	int temp;
	int result;
	cin >> result;
	for (int i = 0; i < N - 1; i++) {
		cin >> temp;
		a.push_back(temp);
	}
	for (int i = 0; i < 4; i++) {
		cin >> temp;
		o.push_back(temp);
	}
	Operator(0,result);
	cout << Max << "\n" << Min;
}