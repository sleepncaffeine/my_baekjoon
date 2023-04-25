#include <bits/stdc++.h>

using namespace std;

typedef struct crd
{
    int x,y;
}crd;

bool cmpr(crd a,crd b)
{
    if(a.x==b.x)
        return a.y<b.y;
    return a.x<b.x;
}

int main()
{
    int n;
    crd point[100001];
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>point[i].x>>point[i].y;
    sort(point,point+n,cmpr);
    for(int i=0;i<n;i++)
        cout<<point[i].x<<" "<<point[i].y<<"\n";
    return 0;
}
