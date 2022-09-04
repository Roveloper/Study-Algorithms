// 오리의 울음 소리 quack
// 동시에 발생되는 quack의 개수를 찾는 문제

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int find(string ducks[], char a) {
    for (int i = 0; i < 2500; i++) {
        if (ducks[i][ducks[i].length() - 1] == a) {
                return i;
            }

    }

    return -1;
}

int main() {
    string sound;
    cin >> sound;

    int max_cnt = 0;
    int duck_cnt = 0;
    string duck_number[2500]; // "qu", "qua", "quac", "q", " ", " "

    for (int i = 0; i < 2500; i++) {
        duck_number[i] = " ";
    }
    // int tmp = 0;
    for (int i = 0; i < sound.length(); i++) {
        if (sound[i] == 'q') {
            auto tmp = find(duck_number, ' ');
            if (tmp == -1) {
                max_cnt = -1;
                break;
            }
            duck_number[tmp] = "q";
            ++duck_cnt;
            if (max_cnt < duck_cnt) {
                max_cnt = duck_cnt;
            }
        }
        else if (sound[i] == 'u') {
            auto tmp = find(duck_number, 'q');
            if (tmp == -1) {
                max_cnt = -1;
                break;
            }
            duck_number[tmp] += "u";
        }
        else if (sound[i] == 'a') {
            auto tmp = find(duck_number, 'u');
            if (tmp == -1) {
                max_cnt = -1;
                break;
            }
            duck_number[tmp] += "a";
        }
        else if (sound[i] == 'c') {
            auto tmp = find(duck_number, 'a');
            if (tmp == -1) {
                max_cnt = -1;
                break;
            }
            duck_number[tmp] += "c";
        }
        else if (sound[i] == 'k') {
            auto tmp = find(duck_number, 'c');
            if (tmp == -1) {
                max_cnt = -1;
                break;
            }
            duck_number[tmp] += "k";
            duck_number[tmp] = " ";
            --duck_cnt;
        }
    }

    for (int i = 0; i < 2500; i++) {
        if (duck_number[i] != " ") {
            max_cnt = -1;
            break;
        }
    }
    cout << max_cnt << endl;

    return 0;
}