#include <bits/stdc++.h>
using namespace std;

int n;
int arr[1000]={0,1,2,};

int main()
{
    cin>>n;
    for(int i=3;i<=n;i++)
        arr[i]=(arr[i-1]+arr[i-2])%10007;
    cout<<arr[n];
    return 0;
}
