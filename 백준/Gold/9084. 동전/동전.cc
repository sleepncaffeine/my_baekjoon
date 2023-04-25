#include <bits/stdc++.h>
using namespace std;

int t;
int coin[20];
int d[10001];

int main()
{
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>coin[i];
        int m;
        cin>>m;
        memset(d,0,sizeof(d));
        d[0]=1;
        for(int i=0;i<n;i++)
        {
            for(int j=coin[i];j<=m;j++)
            {
                d[j]+=d[j-coin[i]];
            }
        }
        cout<<d[m]<<"\n";
    }
    return 0;
}
