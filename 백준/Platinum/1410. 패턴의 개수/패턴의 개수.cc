#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n,k;
int mod=1000003;
int d[50][1<<15];

int main()
{
    cin>>n>>k;
    vector<string> p(n);
    for(int i=0;i<n;i++)
        cin>>p[i];
    int psize=p[0].size();
    for(int i=0;i<psize;i++)
    {
        for(char c='a';c<='z';c++)
        {
            int x=0;
            for(int j=0;j<n;j++)
            {
                if(p[j][i]==c||p[j][i]=='?')
                    x|=(1<<j);
            }
            if(i==0)
                d[i][x]+=1;
            else
            {
                for(int j=0;j<(1<<n);j++)
                {
                    d[i][j&x]=(d[i][j&x]+d[i-1][j])%mod;
                }
            }
        }
    }
    int res=0;
    for(int i=0;i<(1<<n);i++)
    {
        int cnt=0;
        for(int j=0;j<n;j++)
        {
            if(i&(1<<j))
                cnt++;
        }
        if(cnt==k)
        {
            res+=d[psize-1][i];
            res%=mod;
        }
    }
    cout<<res;
    return 0;
}
