#include <bits/stdc++.h>
using namespace std;

int course[1001];
int d[1001]={0,};
int n;

int main()
{
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>course[i];
    for(int i=1;i<n;i++)
    {
        d[i]=-1;
        for(int j=0;j<i;j++)
        {
            if(d[j]!=-1 && i-j<=course[j])
            {
                if(d[i]>d[j]+1 || d[i]==-1)
                    d[i]=d[j]+1;
            }
        }
    }
    cout<<d[n-1]<<endl;
    return 0;
}
