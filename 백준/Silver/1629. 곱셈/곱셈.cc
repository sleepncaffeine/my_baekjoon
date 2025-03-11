#include <iostream>

typedef long long ll;

using namespace std;

ll pow(ll x, ll y, ll z)
{
    ll res = 1;
    while (y)
    {
        if (y & 1)
        {
            res *= x;
            res %= z;
        }
        x *= x;
        x %= z;
        y >>= 1;
    }
    return res % z;
}

int main()
{
    ll a, b, c;
    cin >> a >> b >> c;
    cout << pow(a, b, c) << endl;
    return 0;
}