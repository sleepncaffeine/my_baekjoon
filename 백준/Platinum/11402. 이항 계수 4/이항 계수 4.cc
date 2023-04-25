#include <bits/stdc++.h>
using namespace std;

int modp(long long n,long long r,int p)
{
    int C[r+1];
    memset(C,0,sizeof(C));
    C[0]=1;

    for(long long i=1;i<=n;i++)
    {
        for(int j=min(i,r);j>0;j--)
            C[j]=((C[j]+C[j-1])%p);
    }
    return C[r];
}

long long ncr(long long n,long long r,int p)
{
    if(r==0)
        return 1;
    int ni=n%p,ri=r%p;
    return (ncr(n/p,r/p,p)*modp(ni,ri,p))%p;
}

int main()
{
    long long n,r;
    int p;
    cin>>n>>r>>p;
    cout<<ncr(n,r,p);
    return 0;
}

