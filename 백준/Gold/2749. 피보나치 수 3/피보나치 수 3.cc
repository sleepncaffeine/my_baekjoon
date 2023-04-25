#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll a[1500001];
ll n;
int mod=1000000;

void fibo()
{
    a[0]=0;
    a[1]=1;
    for(int i=0;i<1500000;i++)
        a[i+2]=(a[i]+a[i+1])%mod;
}

int main()
{
    cin>>n;
    fibo();
    cout<<a[n%1500000];
    return 0;
}
