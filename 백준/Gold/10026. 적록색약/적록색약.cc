#include <bits/stdc++.h>

using namespace std;

int n,cnt=0;
char pic[100][100];
bool visited[100][100]={0,};
int dx[]={0,0,-1,1};
int dy[]={-1,1,0,0};

bool isok(int x, int y)
{
    if(x<0||x>=n||y<0||y>=n)
        return false;
    return true;
}

void dfs(int x,int y)
{
    visited[x][y]=true;
    for(int i=0;i<4;i++)
    {
        int nx=x+dx[i];
        int ny=y+dy[i];
        if(!isok(nx,ny))
            continue;
        if(!visited[nx][ny]&&pic[x][y]==pic[nx][ny])
            dfs(nx,ny);
    }
}
int main()
{
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%s",pic[i]);
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(!visited[i][j])
            {
                dfs(i,j);
                cnt++;
            }
        }
    }
    printf("%d ",cnt);
    cnt=0;

    for(int i=0;i<n;i++)
    {

        for(int j=0;j<n;j++)
        {

            if(pic[i][j]=='R')
                pic[i][j]='G';
        }
    }
    memset(visited,false,sizeof(visited));
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(!visited[i][j])
            {
                dfs(i,j);
                cnt++;
            }
        }
    }
    printf("%d",cnt);
    return 0;
}
