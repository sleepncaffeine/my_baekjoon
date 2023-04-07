#include <iostream>
using namespace std;
typedef long long ll;

int arr[1000001];

void prime_find(int m, int n)
{
	for (int i = 2; i <= n; i++)
		arr[i] = i;
	for (int i = 2; i <= n; i++)
	{
		if (arr[i] == 0)
			continue;
		for (int j = i + i; j <= n; j += i)
			arr[j] = 0;
	}
	for (int i = m; i <= n; i++)
	{
		if (arr[i] != 0)
			cout << arr[i] << "\n";
	}
}

int main()
{
	int m, n;
	cin >> m >> n;
	prime_find(m, n);
	return 0;
}