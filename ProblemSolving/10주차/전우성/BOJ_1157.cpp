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

    cin >> s;//????? ??©ö??

    for (i = 0; s[i] != 0; i++) {
        s
            s[i] = toupper(s[i]);
    }
    //????? ?•Ç??? ???

    for (i = 0; i < s.size(); i++) {
        count[s[i] - 65]++;
    }
    //?•Ç??? ????? ????? count

    for (i = 0; i < 26; i++) //'A'???? 'Z' 
    {
        if (max < count[i]) {//max?? ???

            max = count[i];
            position = i;
        }
    }

    int cnt = 0;
    for (i = 0; i < 26; ++i) {
        //cout << count[i]<< endl; count ?ò÷ ???
        if (count[i] == max) {// mac???? ???????? ??? cnt ???????)
            ++cnt;
        }
    }
    if (cnt > 1) {
        cout << "?" << endl;

    }
    else {
        cout << static_cast<char>(position + 65) << endl;//static_cast<char>(position) --> C++ ????? ????!
    }

    return 0;
}