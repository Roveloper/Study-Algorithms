#include <iostream>

int main()
{
	int N;
	
	std::cin >> N;
	
	for (int i=0; i<N; i++)
	{
		std::string S;
		std::cin >> S;
		int total_score = 0;
		int score = 0;
		
		for (int j=0; j<S.size(); j++)
		{
			if (S[j] == 'X')
			{
				score = 0;
			}
			else
			{
				score += 1;
			}
			total_score += score;
		}
		std::cout << total_score << std::endl;
	}
}