#include <bits/stdc++.h>

int main()
{
    int n,x;
    scanf("%d %d",&n,&x);
    int *a=(int *)malloc(sizeof(int)*n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",a+i);
        if(a[i]<x)
            printf("%d ",a[i]);
    }
    return 0;
}
