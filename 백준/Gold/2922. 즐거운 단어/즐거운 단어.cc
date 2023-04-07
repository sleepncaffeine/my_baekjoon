#include <iostream>
#include <cstring>
#include <string>
using namespace std;
typedef long long ll;

string s;
ll d[111][3][3][2];
ll way[3] = { 0, 5, 20 };

int wut(char x)
{
    if (x == 'A' || x == 'E' || x == 'I' || x == 'O' || x == 'U')
        return 1;
    else
        return 2;
}

long long go(int i, int p1, int p2, int l)
{
    if (i == s.length())
    {
        if (l == 1)
            return 1;
        else
            return 0;
    }
    
    ll& ans = d[i][p1][p2][l];
    if (ans != -1) return ans;
    ans = 0;

    if (s[i] != '_')
    {
        if (p1 == p2 && p2 == wut(s[i])) return 0;
        ans = go(i + 1, p2, wut(s[i]), (l | (s[i] == 'L')));
        return ans;
    }

    for (int j = 1; j <= 2; j++)
    {
        if (p1 == p2 && p2 == j) continue;
        ans += way[j] * go(i + 1, p2, j, l);
    }

    if (p1 != p2 || p2 != 2)
        ans += go(i + 1, p2, 2, 1);

    return ans;
}

int main()
{
    cin >> s;
    memset(d, -1, sizeof(d));
    cout << go(0, 0, 0, 0);
    return 0;
}