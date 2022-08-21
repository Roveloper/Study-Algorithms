#include <string>
#include <iostream>
using namespace std;

int main() {

    string s;
    int i;
    int count[26] = { 0, };
    int position = 0;
    int max = 0;
    char c;

    cin >> s;//문자열 입력받기

    for (i = 0; s[i] != 0; i++) {s
        s[i] = toupper(s[i]);
    }
    //소문자 대문자로 변환

    for (i = 0; i < s.size(); i++) {
        count[s[i] - 65]++;
    }
    //대문자로 변환한 함수를 count

    for (i = 0; i < 26; i++) //'A'부터 'Z' 
    {
        if (max < count[i]) {//max값 변환

            max = count[i];
            position = i;
            }
        }
    
    int cnt = 0;
    for (i = 0; i < 26; ++i) {
        //cout << count[i]<< endl; count 배열 확인
        if (count[i] == max) {// mac값이 여러개일 경우 cnt 증가시킴)
            ++cnt;
        }
    }
    if (cnt > 1) {
        cout << "?" << endl;

    }
    else {
        cout << static_cast<char>(position + 65) << endl;//static_cast<char>(position) --> C++ 형변환 주의!
    }
   
        return 0;
}