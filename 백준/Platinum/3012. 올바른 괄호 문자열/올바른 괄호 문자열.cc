#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
string bracket;
ll mod=100000;
ll d[200][200];
char open[4]="({[";
char close[4]=")}]";

ll solve(int i,int j)
{
    if(i>j)
        return 1;
    ll &ans=d[i][j];
    if(ans!=+-1)
        return ans;
    ans=0;
    for(int k=i+1;k<=j;k+=2)
    {
        for(int l=0;l<3;l++)
        {
            if(bracket[i]==open[l]||bracket[i]=='?')
            {
                if(bracket[k]==close[l]||bracket[k]=='?')
                {
                    ll tmp=solve(i+1,k-1)*solve(k+1,j);
                    ans+=tmp;
                    if(ans>=mod)
                        ans=mod+ans%mod;
                }
            }
        }
    }
    return ans;
}

int main()
{
    cin>>n;
    cin>>bracket;
    memset(d,-1,sizeof(d));
    ll res=solve(0, n-1);
    if(res>=mod)
        printf("%05lld",res%mod);
    else
        cout<<res;
    return 0;
}
