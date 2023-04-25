#include <bits/stdc++.h>
using namespace std;

long long f[101];
long long g[101];
long long h[101];
int t;

int main()
{
    f[0]=f[1]=g[1]=h[1]=1;
    g[0]=h[0]=0;
    for(int i=2;i<=100;i++)
    {
        f[i]=f[i-1]+f[i-2]+h[i-1]*2+g[i-1];
        g[i]=f[i-1]+g[i-2];
        h[i]=f[i-1]+h[i-1];
    }
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin>>n;
        cout<<f[n]<<'\n';
    }
    return 0;
}
