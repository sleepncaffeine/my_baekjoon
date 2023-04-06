#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    int n;
    int d[51];
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>d[i];
    sort(d,d+n);
    cout<<d[0]*d[n-1];
    return 0;
}
