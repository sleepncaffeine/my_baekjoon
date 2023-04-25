#include <bits/stdc++.h>
using namespace std;

int d[2][101][21];
string s;
string br[2];

int main()
{
    d[0][0][0]=1; d[1][0][0]=1;
    cin>>s;
    cin>>br[0]>>br[1];
    int n=s.size();
    int m=br[0].size();
    s=" "+s;
    br[0]=" "+br[0]; br[1]=" "+br[1];

    for(int j=1;j<=n;j++)
    {
        for(int i=1;i<=m;i++)
        {
            for(int k=0;k<2;k++)
            {
                if(br[k][i]!=s[j])
                    continue;
                for(int l=i-1;l>=0;l--)
                {
                    if(br[1-k][l]==s[j-1])
                    {
                        d[k][i][j]+=d[1-k][l][j-1];
                    }
                }
            }
        }
    }

    int res=0;
    for(int k=0;k<2;k++)
    {
        for(int i=1;i<=m;i++)
        {
            res+=d[k][i][n];
        }
    }
    cout<<res;
    return 0;
}
