#include <string>
#include <iostream>


int count = 0;
int result = 0;

void ox(char s[], int j) {//OX??? ????
    if (s[j] == 'O') {//'O'??? count ????
        count++;
    }
    else if (s[j] == 'X') {//'X'??? count=0
        count = 0;
    }
    result += count;

}
int main() {


    int n;
    int i = 0;
    char s[80];



    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> s;
        for (int j = 0; s[j] != 0; j++) {
            ox(s, j);
        }
        std::cout << result << std::endl;
        result = 0;
        count = 0;

    }


}