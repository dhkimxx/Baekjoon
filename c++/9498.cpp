#include <iostream>

int main()
{
	int score;
	std::cin >> score;

	switch (score/10)
	{
	case 10:
		std::cout << "A";
		break;
	case 9:
		std::cout << "A";
		break;
	case 8:
		std::cout << "B";
		break;
	case 7:
		std::cout << "C";
		break;
	case 6:
		std::cout << "D";
		break;
	default:
		std::cout << "F";
		break;
	}

}	