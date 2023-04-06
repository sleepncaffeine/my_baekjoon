#include <bits/stdc++.h>

using namespace std;

bool ispal(char str[])
{
    bool is=true;
    int len=strlen(str);
    for(int i=0;i<len/2;i++)
    {
        if(str[i]!=str[len-i-1])
            is=false;
    }
    if(is)
        return true;
    else
        return false;
}

int main()
{
    char str[6];
    while(1)
    {
        scanf("%s",str);
        if(str[0]=='0'&&str[1]=='\0')
            break;
        if(ispal(str))
            printf("yes\n");
        else
            printf("no\n");
    }
    return 0;
}
