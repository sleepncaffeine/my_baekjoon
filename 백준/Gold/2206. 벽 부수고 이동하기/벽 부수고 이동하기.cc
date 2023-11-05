#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1005;
int N, M;
int dist[MAXN][MAXN][2];
int grid[MAXN][MAXN];

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

struct State
{
    int x, y, b;
};

bool isValid(int x, int y)
{
    return (x >= 1 && x <= N && y >= 1 && y <= M);
}

int bfs() {
    memset(dist, -1, sizeof(dist));
    dist[1][1][0] = 1;
    queue<State> q;
    q.push({1, 1, 0});

    while (!q.empty())
    {
        State curr = q.front();
        q.pop();

        if (curr.x == N && curr.y == M)
        {
            return dist[curr.x][curr.y][curr.b];
        }

        for (int i = 0; i < 4; i++) 
        {
            int nx = curr.x + dx[i];
            int ny = curr.y + dy[i];
            if (isValid(nx, ny)) {
                if (grid[nx][ny] == 0 && dist[nx][ny][curr.b] == -1) 
                {
                    dist[nx][ny][curr.b] = dist[curr.x][curr.y][curr.b] + 1;
                    q.push({nx, ny, curr.b});
                }
                else if (grid[nx][ny] == 1 && curr.b == 0 && dist[nx][ny][1] == -1) 
                {
                    dist[nx][ny][1] = dist[curr.x][curr.y][0] + 1;
                    q.push({nx, ny, 1});
                }
            }
        }
    }

    return -1;
}

int main() 
{
    cin >> N >> M;

    for (int i = 1; i <= N; i++) 
    {
        for (int j = 1; j <= M; j++) 
        {
            char c;
            cin >> c;
            grid[i][j] = c - '0';
        }
    }

    int ans = bfs();
    cout << ans << endl;

    return 0;
}
