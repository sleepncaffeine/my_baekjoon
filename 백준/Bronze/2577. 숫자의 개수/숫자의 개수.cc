#include <bits/stdc++.h>

using namespace std;

int main()
{
    int num[10]={0,};
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    long long d=(a*b*c);
    while(d>0)
    {
        int tmp=(d%10);
        num[tmp]++;
        d/=10;
    }
    for(int i=0;i<10;i++)
        printf("%d\n",num[i]);
    return 0;
}
