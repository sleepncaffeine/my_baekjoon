#include <bits/stdc++.h>
using namespace std;

int n,last,first;
int period,cnt=1;
vector<pair<int,int>> clndr;

int main()
{
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>first>>last;
        clndr.push_back(make_pair(last,first));
    }
    sort(clndr.begin(),clndr.end());
    period=clndr[0].first;
    for(int i=1;i<n;i++)
    {
        if(period<=clndr[i].second)
        {
            cnt++;
            period=clndr[i].first;
        }
    }
    cout<<cnt;
    return 0;
}
