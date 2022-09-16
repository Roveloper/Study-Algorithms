#include <iostream>
using namespace std;
int d(int x);
int a[10000];

int main() {

	for (int i = 0; i < 10000; i++) {
		a[i] = i + 1;
	}
	for (int i = 0; i < 10000; i++) {
		a[d(i + 1) + i] = 0;
	}
	for (int i = 0; i < 10000; i++) {
		if (a[i] != 0) {
			cout << a[i] << "\n";
		}
	}
	return 0;
}

int d(int x)
{
	int ans = 0;
	int sum = 0;

	while (x > 0) {
		ans = x % 10;
		x = x / 10;
		sum = sum + ans;

	}
	return sum;
}