#include <bits/stdc++.h>
using namespace std;

int n,blue,white;
int paper[130][130];

void dfs(int x,int y,int keugi)
{
    bool a=true,b=true;
    for(int i=x;i<x+keugi;i++)
    {
        for(int j=y;j<y+keugi;j++)
        {
            if(paper[i][j]==1)
                a=false;
            if(paper[i][j]==0)
                b=false;
        }
    }
    if(a)
    {
        white++;
        return;
    }
    if(b)
    {
        blue++;
        return;
    }
    int s=keugi/2;
    dfs(x,y,s);
    dfs(x,y+s,s);
    dfs(x+s,y,s);
    dfs(x+s,y+s,s);
}

int main()
{
    cin>>n;
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            cin>>paper[i][j];
    dfs(0,0,n);
    cout<<white<<"\n"<<blue;
    return 0;
}
