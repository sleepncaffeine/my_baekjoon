#include <bits/stdc++.h>
using namespace std;

int n,r,c;
int ans=0;

void calc(int x,int y,int kugi)
{
    if(x==c&&y==r)
    {
        cout<<ans;
        return;
    }
    if(c<x+kugi && r<y+kugi && c>=x && r>=y)
    {
        calc(x,y,kugi/2);
        calc(x,y+kugi/2,kugi/2);
        calc(x+kugi/2,y,kugi/2);
        calc(x+kugi/2,y+kugi/2,kugi/2);
    }
    else
        ans+=kugi*kugi;
}

int main()
{
    cin>>n>>c>>r;
    calc(0,0,1<<n);
    return 0;
}
