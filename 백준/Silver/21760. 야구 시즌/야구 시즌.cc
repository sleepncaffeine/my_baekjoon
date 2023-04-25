#include <bits/stdc++.h>
using namespace std;

int t,n,m,k;
long int d;
int a,b,game,x;

int main()
{
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        b=0;
        scanf("%d %d %d %ld",&n,&m,&k,&d);
        x=2*d/(n*m*(m-1)*k+n*(n-1)*m*m);
        while(b<x)
            b++;
        if(b==0)
            printf("-1\n");
        else
            printf("%d\n",(n*m*(m-1)*k*b+n*(n-1)*m*m*b)/2);
    }
    return 0;
}
