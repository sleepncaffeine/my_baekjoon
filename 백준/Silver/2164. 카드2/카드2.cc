#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    queue<int> q;
    cin>>n;
    for(int i=1;i<=n;i++)
        q.push(i);
    while(q.size()>1)
    {
        q.pop();
        int tmp;
        tmp=q.front();
        q.push(tmp);
        q.pop();
    }
    cout<<q.front();
    return 0;
}
