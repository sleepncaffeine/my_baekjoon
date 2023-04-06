#include <bits/stdc++.h>

using namespace std;

int asdf[41]={0,};

int fibo(int n)
{
    if(asdf[n]!=0)
        return asdf[n];
    if(n<=0)
        return 0;
    else if(n==1)
    {
        asdf[1]=1;
        return 1;
    }
    else
        return asdf[n]=fibo(n-1)+fibo(n-2);
}

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin>>n;
        if(n==0)
            printf("1 0\n");
        else if(n==1)
            printf("0 1\n");
        else
        {
            fibo(n);
            printf("%d %d\n",asdf[n-1],asdf[n]);
        }
    }
    return 0;
}
