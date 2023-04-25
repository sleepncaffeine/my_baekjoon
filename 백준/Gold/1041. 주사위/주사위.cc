#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int a[6];
int m1,m2,m3;
ll n,n1,n2,n3=4,sum=0;

int main()
{
    cin>>n;
    for(int i=0;i<6;i++)
        cin>>a[i];
    if(n==1)
    {
        sort(a,a+6);
        for(int i=0;i<5;i++)
            sum+=a[i];
    }
    else
    {
        a[0]=min(a[0],a[5]);
        a[1]=min(a[1],a[4]);
        a[2]=min(a[2],a[3]);
        sort(a,a+3);

        n1=4*(n-1)*(n-2)+(n-2)*(n-2);
        n2=4*(n-1)+4*(n-2);
        m1=a[0];
        m2=a[0]+a[1];
        m3=a[0]+a[1]+a[2];

        sum+=n1*m1;
        sum+=n2*m2;
        sum+=n3*m3;
    }
    cout<<sum;
    return 0;
}
