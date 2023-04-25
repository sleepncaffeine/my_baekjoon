#include <bits/stdc++.h>

using namespace std;

int main()
{
    int k,n,ans=0;
    int maxi=0;
    int lan[10001];
    long long high,mid,low;

    cin>>k>>n;
    for(int i=0;i<k;i++)
    {
        cin>>lan[i];
        if(lan[i]>maxi)
            maxi=lan[i];
    }
    high=maxi;
    low=1;
    while(low<=high)
    {
        int tmp=0;
        mid=(low+high)/2;
        for(int i=0;i<k;i++)
            tmp+=lan[i]/mid;
        if(tmp>=n)
        {
            low=mid+1;
            if(ans<mid)
                ans=mid;
        }
        else
            high=mid-1;
    }
    cout<<ans;
    return 0;
}
