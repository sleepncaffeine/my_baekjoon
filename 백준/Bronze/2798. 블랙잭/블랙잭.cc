#include <bits/stdc++.h>

using namespace std;

int n,m;
int card[100];

int main()
{
    scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++)
        scanf("%d",&card[i]);
    int maxi=-1;
    int sum=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(i==j) continue;
            for(int k=0;k<n;k++)
            {
                if(i==k||j==k) continue;
                sum=0;
                sum+=card[i]+card[j]+card[k];
                if(sum>m) continue;
                if(maxi<sum) maxi=sum;
            }
        }
    }
    printf("%d",maxi);
    return 0;
}
