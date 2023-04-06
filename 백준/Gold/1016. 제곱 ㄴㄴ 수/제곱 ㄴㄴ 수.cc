#include <bits/stdc++.h>
using namespace std;

long long num[1000001];
long long mini,maxi;
int cnt=0;

int main()
{
    cin>>mini>>maxi;
    for(long long i=2;i*i<=maxi;i++)
    {
        long long a=mini/(i*i);
        if(mini%(i*i))
            a++;
        while(i*i*a<=maxi)
        {
            num[i*i*a-mini]=1;
            a++;
        }
    }
    for(long long i=0;i<=maxi-mini;i++)
        if(num[i]==0)
            cnt++;
    cout<<cnt;
    return 0;
}
