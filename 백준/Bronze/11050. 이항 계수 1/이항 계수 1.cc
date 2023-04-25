#include <stdio.h>

int r,n,res=1;

int main()
{
    scanf("%d %d",&n,&r);
    int k=n;
    for(int i=0;i<r;i++)
    {
        res*=k;
        k--;
    }
    for(int i=1;i<=r;i++)
        res/=i;
    printf("%d",res);

    return 0;
}
