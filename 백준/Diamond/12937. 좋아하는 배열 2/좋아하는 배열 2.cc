#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

using namespace std;

const ll mod = 1000000007;

ll yay[50001];
ll nay[50001];
ll kpw[50001];
ll dvs[21];
ll d[21][50001];
int n, k;

int main() 
{
    cin >> n >> k;
    kpw[0] = 1;
    nay[0] = 0;
    yay[0] = 1;

    for (int i = 1; i <= n; i++)
        kpw[i] = (k * kpw[i - 1]) % mod;

    for (int j = 0; j <= k; j++)
        d[1][j] = 1;

    for (int i = 2; i <= 20; i++) 
    {
        for (int l = 1; l <= k; l++)
        {
            for (int j = 2 * l; j <= k; j += l)
                d[i][j] += d[i - 1][l];
        }
        for (int j = 0; j <= k; j++) 
        {
            dvs[i] += d[i][j];
            dvs[i] %= mod;
        }
    }

    for (int i = 1; i <= n; i++) 
    {
        nay[i] = (nay[i - 1] * k) % mod;
        for (int j = 2; j <= i && j <= 20; j++)
        {
            ll tmp = 1;
            if (j % 2 == 1)
                tmp = mod - 1;

            ll x = tmp;
            ll y = yay[i - j];
            ll z = dvs[j];
            nay[i] += (((x * y) % mod) * z) % mod;
        }
        nay[i] %= mod;
        yay[i] = (kpw[i] + mod - nay[i]) % mod;
    }

    cout << yay[n] << '\n';
    return 0;
}