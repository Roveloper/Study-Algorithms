#include <iostream>
using namespace std;
int main() {
	int n;
	char a[400][400];
	
	cin >> n;
	int k = 0;
	
	for (int z = 0; z < n; z++) {
		for (int i = k; i < 4 * n - 3 - k; i++) {
			for (int j = k; j < 4 * n - 3 - k; j++) {
				if (i == k || i == 4 * n - 4 - k) {
					a[i][j] = '*';
				}
				else {
					if (j == k || j == 4 * n - 4 - k)
						a[i][j] = '*';
					else
						a[i][j] = ' ';
				}
			}
		}
		
		k = k + 2;
		
	}

	for (int i = 0; i < 4 * n - 3; i++) {
		for (int j = 0; j < 4 * n - 3; j++) {
			cout << a[i][j];
		}
		cout << endl;
	}
	
	return 0;
}
