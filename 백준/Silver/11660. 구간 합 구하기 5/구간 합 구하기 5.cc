#include <bits/stdc++.h>
using namespace std;

int dp[1025][1025] = {};
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int N, M;
    int temp;
    cin >> N >> M;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            cin >> temp;
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + temp - dp[i - 1][j - 1];
        }
    }

    int x1, y1, x2, y2;

    for (int i = 0; i < M; i++)
    {
        int ans = 0;
        cin >> x1 >> y1 >> x2 >> y2;
        ans = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1];
        cout << ans << '\n';
    }

    return 0;
}