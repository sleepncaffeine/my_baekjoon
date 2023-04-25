#include <bits/stdc++.h>

using namespace std;

int n,l;
long long int k;
long long int bn[32][32];

int main()
{
    scanf("%d %d %lld",&n,&l,&k);
    for(int i=0;i<32;i++)
        bn[0][i]=1;
    for(int i=1;i<32;i++)
    {
        bn[i][0]=bn[i-1][0];
        for(int j=1;j<32;j++)
        {
            bn[i][j]=bn[i-1][j-1]+bn[i-1][j];
        }
    }
    while(n>0)
    {
        if(k<=bn[n-1][l])
        {
            printf("0");
            n--;
        }
        else
        {
            printf("1");
            k-=bn[n-1][l];
            n--;
            l--;
        }
    }
    printf("\n");
    return 0;
}
