#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n,m;
    int mini=99999;
    int b=0,w=0;
    char chess[50][50];

    scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++)
        scanf("%s",&chess[i]);

    for(int i=0;i<n-7;i++)
    {
        for(int j=0;j<m-7;j++)
        {
            b=0; w=0;
            for(int x=i;x<i+8;x++)
            {
                for(int y=j;y<j+8;y++)
                {
                    if((x+y)%2==0)
                    {
                        if(chess[x][y]=='B')
                            w++;
                        else
                            b++;
                    }
                    else
                    {
                        if(chess[x][y]=='B')
                            b++;
                        else
                            w++;
                    }
                }
            }
            mini=min(mini,b);
            mini=min(mini,w);
        }
    }
    printf("%d",mini);
    return 0;
}
