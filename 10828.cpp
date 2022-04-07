#include <iostream>
#include <vector>
using namespace std;

vector <int> stack;

int size() {
	int sum = 0;
	for (int i : stack) {
		sum++;
	}
	return sum;
}
int empty() {
	if (size() == 0)
		return 1;
	else
		return 0;
}
int top() {
	if (empty())
		return -1;
	else {
		return stack[size() - 1];
	}
}
int pop() {
	if (empty())
		return -1;
	else {
		int temp = top();
		stack.pop_back();
		return temp;
	}
}
int push() {
	int x;
	cin >> x;
	stack.push_back(x);
	return 0;
}

int main() { 
	int N; cin >> N;
	for (int i = 0; i < N; i++) {
		string temp;
		cin >> temp;
		if (temp == "push") {
			push();
		}
		if (temp == "pop") {
			cout << pop() << "\n";
		}
		if (temp == "size") {
			cout << size() << "\n";
		}
		if (temp == "empty") {
			cout << empty() << "\n";
		}
		if (temp == "top") {
			cout << top() << "\n";
		}
	}
}