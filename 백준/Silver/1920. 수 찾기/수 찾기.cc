#include <bits/stdc++.h>

using namespace std;

int number[10000001],m,question[100001];
long long int n;

int Bsearch(int target,int low,long long int high)
{
    if(low>high)
        return 0;
    int mid=(low+high)/2;
    if(number[mid]==target)
        return 1;
    else if(number[mid]>target)
        return Bsearch(target,low,mid-1);
    else
       return Bsearch(target,mid+1,high);
}

bool arr(int x,int y)
{
    return x<y;
}

int main()
{
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&number[i]);
    }
    sort(number,number+n,arr);
    scanf("%d",&m);
    for(int i=0;i<m;i++){
        scanf("%d",&question[i]);
    }
    for(int i=0;i<m;i++){
        printf("%d\n",Bsearch(question[i],0,n-1));
    }
    return 0;
}
