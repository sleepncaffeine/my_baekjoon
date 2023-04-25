#include <bits/stdc++.h>
using namespace std;

long long fibo[41];
int n;

int main()
{
    fibo[1]=1;
    fibo[2]=1;
    for(int i=3;i<41;i++)
        fibo[i]=fibo[i-1]+fibo[i-2];
    cin>>n;
    cout<<fibo[n]<<" "<<n-2;
    return 0;
}
