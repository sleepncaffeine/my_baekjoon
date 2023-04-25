#include <bits/stdc++.h>
using namespace std;

int n,m;
int d[1001][1001];
int men[1001];
int wom[1001];

int main()
{
    cin>>n>>m;
    for(int i=1;i<=n;i++)
        cin>>men[i];
    for(int i=1;i<=m;i++)
        cin>>wom[i];
    sort(men+1,men+n+1);
    sort(wom+1,wom+m+1);
    if(n>m)
    {
        swap(n,m);
        swap(men,wom);
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=i;j<=m;j++)
        {
            d[i][j]=d[i-1][j-1]+abs(men[i]-wom[j]);
            if(d[i][j]>d[i][j-1] && i<=j-1)
                d[i][j]=d[i][j-1];
        }
    }
    cout<<d[n][m];
    return 0;
}
