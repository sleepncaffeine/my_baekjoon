#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

int a[100];
int d[100][100][5];
int n, m;

int go(int l, int r, int c)
{
    if (l > r) 
        return 0;
    if (l == r) 
        return m - 1 - c;
    int& ans = d[l][r][c];
    if (ans != -1) 
        return ans;
    ans = 0;
    if (c < m - 1)
        ans = go(l, r, c + 1) + 1;
    if (c == m - 1)
        ans = go(l + 1, r, 0);

    for (int i = l + 1; i <= r; i++) 
    {
        if (a[i] != a[l]) 
            continue;
        int temp = go(l + 1, i - 1, 0) + go(i, r, min(m - 1, c + 1));
        if (ans > temp) 
            ans = temp;
    }
    return ans;
}

int main() 
{
    memset(d, -1, sizeof(d));
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        cin >> a[i];

    cout << go(0, n - 1, 0) << '\n';

    return 0;
}
