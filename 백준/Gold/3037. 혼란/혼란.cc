#include <iostream>
using namespace std;
typedef long long ll;

ll d[1001][10001];
const ll mod = 1000000007;

int main()
{
    int n, k;
    cin >> n >> k;
    d[1][0] = 1;

    for (int i = 2; i <= n; i++)
    {
        for (int j = 0; j <= k; j++)
        {
            d[i][j] = d[i - 1][j];
            if (j - 1 >= 0)
                d[i][j] = (d[i][j] + d[i][j - 1]) % mod;
            
            if (j >= i)
                d[i][j] = (d[i][j] - d[i - 1][j - i] + mod) % mod;
        }
    }

    cout << d[n][k];
    return 0;
}