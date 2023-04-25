#include <bits/stdc++.h>

using namespace std;

int main()
{
    int scale[9];
    int asc=1,des=1;
    for(int i=0;i<8;i++)
        scanf("%d",&scale[i]);
    for(int i=0;i<8;i++)
        if(scale[i]!=i+1)
        {
            asc=0;
            break;
        }
    for(int i=0;i<8;i++)
        if(scale[i]!=8-i)
        {
            des=0;
            break;
        }
    if(asc==0&&des==0)
        printf("mixed");
    else if(asc==1)
        printf("ascending");
    else
        printf("descending");
    return 0;
}
