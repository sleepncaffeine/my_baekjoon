#include <bits/stdc++.h>
using namespace std;

int d[1001][1001];
int a[1001][1001];
int res=0;

int main()
{
    int n,m;
    cin>>n>>m;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            scanf("%1d",&a[i][j]);
        }
    }

    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            if(a[i][j]==0)
                continue;
            d[i][j]=min({d[i-1][j-1],d[i-1][j],d[i][j-1]})+1;
            if(res<d[i][j])
                res=d[i][j];
        }
    }
    cout<<res*res;
    return 0;
}
