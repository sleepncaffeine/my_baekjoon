#include <bits/stdc++.h>

using namespace std;

//[n,k] = ([n-1,k]+k-1)%n + 1

int n,k,ans=0;

int main()
{
    cin>>n>>k;
    for(int i=1;i<=n;i++)
        ans=(ans+k-1)%i+1;
    cout<<ans;
    return 0;
}
