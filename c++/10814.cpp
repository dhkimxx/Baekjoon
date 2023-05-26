#include <iostream>
#include <algorithm>

struct Member
{
	int age, id;
	std::string name;
};

int compare(Member a, Member b) {
	if (a.age == b.age) return a.id < b.id;
	return a.age < b.age;
}

int main() {
	int N; std::cin >> N;
	Member *member = new Member[N];
	for (int i = 0; i < N; i++) {
		std::cin >> member[i].age >> member[i].name;
		member[i].id = i;
	}
	std::sort(member, member + N, compare);
	for (int i = 0; i < N; i++) {
		std::cout << member[i].age << " " << member[i].name << "\n";
	}
}