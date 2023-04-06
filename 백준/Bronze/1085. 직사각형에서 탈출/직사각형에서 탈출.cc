#include <bits/stdc++.h>

using namespace std;

int x,y,w,h;

int main()
{
    scanf("%d%d%d%d",&x,&y,&w,&h);
    int dist;
    dist = min(x,min(y,min(w-x,h-y)));
    printf("%d",dist);
    return 0;
}
