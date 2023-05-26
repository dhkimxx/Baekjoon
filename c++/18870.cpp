#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int N; cin >> N;
	vector<int> v, vcp;
	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		v.push_back(temp);
		vcp.push_back(temp);
	}
	sort(vcp.begin(),vcp.end());
	vcp.erase(unique(vcp.begin(), vcp.end()), vcp.end());
	for (int i : v) {
		int pos = lower_bound(vcp.begin(), vcp.end(), i) - vcp.begin();
		cout << pos << " ";
	}
	return 0;
}