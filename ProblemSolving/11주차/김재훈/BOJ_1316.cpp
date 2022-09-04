#include <iostream>
#include <set>
#include <unordered_set>

using namespace std;

int main()
{
    int N;
    cin >> N;

    // cout << N <<" " << typeid(N).name() << endl;

    int result = 0;
    for (int i = 0; i < N; i++)
    {
        string word;
        // set<char> unique_char;
        unordered_set<char> unique_char;
        cin >> word;
        int cnt = 1;
        char now = word[0];
        unique_char.insert(now);
        for (int j = 1; j < word.size(); j++)
        {
            if (now != word[j])
            {
                ++cnt;
                now = word[j];
                unique_char.insert(now);
            }
        }
        
        if (cnt == unique_char.size())
        {
            ++result;
        }
    }

    cout << result << endl;

    return 0;
}