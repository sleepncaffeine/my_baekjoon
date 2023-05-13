#include <bits/stdc++.h>
using namespace std;

int dp[101][100001];

int main()
{
	vector<pair<int, int>> asdf;
	int N, K;
	cin >> N >> K;
	asdf.resize(N + 1);

	for (int i = 1; i <= N; i++)
    {
		int x, y;
		cin >> x >> y;
		asdf[i] = { x, y };
	}

	for (int i = 1; i <= N; i++)
    {
		for (int j = 1; j <= K; j++)
        {
			if (j >= asdf[i].first) dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - asdf[i].first] + asdf[i].second);
			else dp[i][j] = dp[i - 1][j];
		}
	}
	cout << dp[N][K];

    return 0;
}