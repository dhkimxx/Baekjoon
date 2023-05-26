#include <iostream>

int main()
{
	int h, m, h_t, m_t;

	std::cin >> h >> m;

	if (m >= 45) {
		m_t = m - 45;
		h_t = h;
	}
	else {
		m_t = m - 45 + 60;
		if (h == 0)
			h_t = 23;
		else
			h_t = h - 1;
	}
		
	std::cout << h_t << " " << m_t;
	return 0;
}