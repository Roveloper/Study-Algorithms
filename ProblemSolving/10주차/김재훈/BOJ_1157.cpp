#include <iostream>
#include <string>
#include <algorithm>

int main()
{
	std::string S;
	std::cin >> S;
	int cnt[26];
	
	for (int i=0; i<S.size(); i++)
	{
		S[i] = toupper(S[i]);
	}
//	std::cout << static_cast<char>(65) << std::endl;
//	int i = S.find(static_cast<char>(65), 5);
//	std::cout << i << std::endl;
	
	for (int i=0; i<26; i++)
	{
		int idx = 0;
		cnt[i] = 0;
		while (S.find(static_cast<char>(i + 65), idx) != -1)
		{
			idx = S.find(static_cast<char>(i + 65), idx) + 1;
			cnt[i] += 1;
		}
		
		
	}
	
	int* max_ptr = std::max_element(std::begin(cnt), std::end(cnt));
	int max_cnt = *max_ptr;
	char answer = static_cast<char>(65 + std::distance(cnt, max_ptr));
	*max_ptr = 0;	
	max_ptr = std::max_element(std::begin(cnt), std::end(cnt));
	
	if (max_cnt == *max_ptr)
	{
		std::cout << "?" << std::endl;
	}
	else
	{
		std::cout << answer << std::endl;
	}
	    
	return 0;
}
	
 	
	