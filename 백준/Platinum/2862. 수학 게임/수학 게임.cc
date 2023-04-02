#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll n;
vector<ll> fibo;

int main()
{
    cin>>n;
    ll x=1,y=1;
    while(y<=n)
    {
        fibo.push_back(y);
        ll tmp=y;
        y+=x;
        x=tmp;
    }

    //Zeckendorf
    ll asdf;
    for(int i=fibo.size()-1;i>=0;i--)
    {
        if(fibo[i]-n<=0)
        {
            asdf=fibo[i];
            n-=asdf;
        }
    }
    cout<<asdf;
    return 0;
}
