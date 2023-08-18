#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

int eulerphi(int n)
{
    int euler = n;
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
            euler = euler / i * (i - 1);
        while (n % i == 0)
            n /= i;
    }
    if (n == 1)
        return euler;
    else
        return euler / n * (n - 1);
}

int calc(int n, int m)
{
    if (n == 1 || m == 1)
        return 1;
    ll a = n;
    int b = calc(n, eulerphi(m)) + eulerphi(m);
    int res = 1;
    while (b)
    {
        if (b & 1)
            res = res * a % m;
        b >>= 1;
        a = a * a % m;
    }
    return res;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n >> m;
        cout << int(calc(n, m) % m) << endl;
    }
    return 0;
}
