#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n_and_m(int end, int max_depth, vector<int> stack) {
	if (max_depth > 0) {
		for (int i = 1; i <= end; i++) {
			auto id = find(stack.begin(), stack.end(), i);
			if (id == stack.end()) {
				stack.push_back(i);
				n_and_m(end, --max_depth, stack);
				stack.pop_back();
				++max_depth;
			}
			else {
				continue;
			}
		}
		return 0;
	}
	else {
		for (int loop : stack) {
			cout << loop << " ";
		}
		cout << "\n";
		return 0;
	}	
}

int main() {
	int N, M; cin >> N >> M;
	vector<int> stack;
	n_and_m(N, M, stack);
}