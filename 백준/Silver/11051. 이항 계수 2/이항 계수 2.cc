#include <bits/stdc++.h>
using namespace std;

int mod=10007;
int d[1001][1001];
int n,k;

int main()
{
    cin>>n>>k;
    for(int i=0;i<=n;i++)
    {
        d[i][0]=d[i][i]=1;
        for(int j=1;j<=i-1;j++)
        {
            d[i][j]=d[i-1][j-1]+d[i-1][j];
            d[i][j]%=mod;
        }
    }
    cout<<d[n][k];
    return 0;
}
