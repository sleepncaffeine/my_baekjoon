#include <bits/stdc++.h>

using namespace std;

string wrd[20000];

bool cmpr(string x,string y)
{
    if(x.length()==y.length())
        return x<y;
    else
        return x.length()<y.length();
}

int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>wrd[i];
    sort(wrd,wrd+n,cmpr);
    for(int i=0;i<n;i++)
    {
        if(wrd[i]==wrd[i-1])
            continue;
        cout<<wrd[i]<<"\n";
    }
    return 0;
}
