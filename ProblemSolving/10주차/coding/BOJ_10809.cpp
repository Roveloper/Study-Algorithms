#include <string>
#include <iostream>

using namespace std;
int main() {

    string s;
    cin >> s;
    for (int alphabet = 'a'; alphabet <= 'Z'; alphabet++) {
        int position = s.find(alphabet);
        cout << position << " ";
    }
    return 0;
}
