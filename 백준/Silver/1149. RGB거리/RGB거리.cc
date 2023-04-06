#include <bits/stdc++.h>
using namespace std;

int h[1001][3];
int c[1001][3];
int n;

int main()
{
    cin>>n;
    for(int i=1;i<=n;i++)
        cin>>h[i][0]>>h[i][1]>>h[i][2];
    memset(c,0,sizeof(c));
    for(int i=1;i<=n;i++)
    {
        c[i][0]=min(c[i-1][1],c[i-1][2])+h[i][0];
        c[i][1]=min(c[i-1][0],c[i-1][2])+h[i][1];
        c[i][2]=min(c[i-1][0],c[i-1][1])+h[i][2];
    }
    cout<<min({c[n][0],c[n][1],c[n][2]});
    return 0;
}
