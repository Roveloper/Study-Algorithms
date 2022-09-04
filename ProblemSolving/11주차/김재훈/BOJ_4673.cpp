// BOJ 4673 셀프 넘버
// d(n) --> 양의 정수 n에 대해 n과 n의 각 자리수를 더하는 함수
// d(75) = 75 + 7 + 5 = 87
// n이 하나 주어지면, d(n), d(d(n)), d(d(d(n)))과 같은 형식으로 무한 수열이 가능
// 이 때, n을 d(n)의 생성자라고 말할 수 있다. 33은 39의 생성자, 39는 51의 생성자, 51는 57의 생성자
// 생성자는 꼭 1개만 있는 것은 아니다, 101은 생성자가 91과 100 두 개가 있다.
// 셀프 넘버란, 생성자가 없는 숫자를 의미하며, 100보다 작은 셀프 넘버는 총 13개가 있음 --> 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
// 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

#include <iostream>
#include <string>

using namespace std;

int d(const int n) {
    string tmp = to_string(n); // 12345 --> "12345"
    int result = n;
    for (int i = 0; i < tmp.size(); i++) {
        result += static_cast<int>(tmp[i] - '0'); // '1' - '0'
    }
    return result;
}

int main() {
    int numbers[10001];
    fill_n(numbers, 10001, 0);

    // numbers[1] += 1;

    for (int i = 1; i < 10001; i++) {
        int tmp = d(i);
        // cout << tmp << endl;
        if (tmp > 10000) {
            continue;
        }
        numbers[tmp] += 1;
        
    }
    

    for (int i = 1; i < 10001; i++)
    {
        // cout << numbers[i] << endl;
        if (numbers[i] == 0) {
            cout << i << endl;
        }
    }

    return 0;
}
    