#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;

int main()
{
	int n;
	cin >> n;
	vector<int> v(n);
	int cnt = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> v[i];
		if (v[i] % 2 == 0) cnt++;
	}
	int a = 0;
	for (int i = 0; i < n; i++)
	{
		if (v[i] % 2 == 0)
			a += i;
	}
	a -= cnt * (cnt - 1) / 2;

	int b = 0;
	for (int i = 0; i < n; i++)
	{
		if (v[i] % 2 == 1)
			b += i;
	}
	b -= (n - cnt) * (n - cnt - 1) / 2;

	cout << min(a, b) << "\n";
}
