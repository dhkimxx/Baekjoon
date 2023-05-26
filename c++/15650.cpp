#include <iostream>
#include <vector>
using namespace std;

int n_and_m(int end, int max_depth, vector<int> stack) {
	if (max_depth > 0) {
		for (int i = 1; i <= end; i++) {
			if (stack.size() > 0 && stack.back() >= i) // stack의 마지막 보다 크지 않으면 continue
				continue;
			stack.push_back(i);
			n_and_m(end, --max_depth, stack);
			stack.pop_back();
			++max_depth;
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