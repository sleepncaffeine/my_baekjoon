#include <bits/stdc++.h>
using namespace std;

int n;
int a[100],b[100];
int turn[10]={0,1,1,1,2,2,2,1,1,1};
int d[100][10][10];

int solve(int i,int j,int k)
{
    if(i==n)
        return 0;
    if(d[i][j][k]!=-1)
        return d[i][j][k];
    int orig=(a[i]+j)%10;
    int dest=b[i];

    for(int x3=0;x3<10;x3++)
    {
        for(int x2=0;x2<10;x2++)
        {
            int start=(orig+x2+x3)%10;
            int x1=dest-start;
            if(x1<0)
                x1+=10;
            int cost=turn[x1]+turn[x2]+turn[x3];
            cost+=solve(i+1,(k+x2+x3)%10,x3);
            if(d[i][j][k]==-1 || d[i][j][k]>cost)
                d[i][j][k]=cost;
        }
    }
    return d[i][j][k];
}

int main()
{
    cin>>n;
    for(int i=0;i<n;i++)
        scanf("%1d",&a[i]);
    for(int i=0;i<n;i++)
        scanf("%1d",&b[i]);
    for(int i=0;i<n;i++)
        for(int j=0;j<10;j++)
            for(int k=0;k<10;k++)
                d[i][j][k]=-1;
    cout<<solve(0,0,0);
    return 0;
}
