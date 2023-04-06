#include <bits/stdc++.h>
using namespace std;

int n,m;
int baechu;
bool a[51][51];
bool visited[51][51];
int dx[]={0,0,-1,1};
int dy[]={1,-1,0,0};
//baechu white worm!
bool is_in_range(int x,int y)
{
    if(x>=0&&x<m&&y>=0&&y<n)
        return true;
    return false;
}

bool dfs_worm(int y,int x)
{
    if(visited[y][x])
        return false;
    visited[y][x]=true;

    for(int i=0;i<4;i++)
    {
        int nx=x+dx[i];
        int ny=y+dy[i];
        if(is_in_range(nx,ny)&&a[ny][nx])
            dfs_worm(ny,nx);
    }
    return true;
}

int main()
{
    int t;
    int worm=0;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        worm=0;
        memset(visited,0,sizeof(visited));
        memset(a,0,sizeof(a));
        cin>>m>>n>>baechu;
        for(int j=0;j<baechu;j++)
        {
            int x,y;
            cin>>x>>y;
            a[y][x]=1;
        }
        for(int j=0;j<n;j++)
        {
            for(int k=0;k<m;k++)
            {
                if(!visited[j][k]&&a[j][k])
                {
                    if(dfs_worm(j,k))
                        worm++;
                }
            }
        }
        cout<<worm<<"\n";
    }
    return 0;
}
