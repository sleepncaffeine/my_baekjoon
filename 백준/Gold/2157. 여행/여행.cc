#include <bits/stdc++.h>
using namespace std;

int a[301][301];
int d[301][301];
int n,m,k;

int main()
{
    ios_base::sync_with_stdio(false);
    memset(d,-1,sizeof(d));
    d[1][1]=0;
    cin>>n>>m>>k;
    for(int i=0;i<k;i++)
    {
        int p,q,r;
        cin>>p>>q>>r;
        if(a[p][q]<r)
            a[p][q]=r;
    }

    for(int j=1;j<=m-1;j++)
    {
        for(int i=1;i<=n;i++)
        {
            if(d[i][j]==-1)
                continue;
            for(int k=i+1;k<=n;k++)
            {
                if(a[i][k]>0)
                {
                    d[k][j+1]=max(d[k][j+1],d[i][j]+a[i][k]);
                }
            }
        }
    }
    int res=0;
    for(int i=2;i<=m;i++)
    {
        if(d[n][i]>res)
            res=d[n][i];
    }
    cout<<res;
    return 0;
}
