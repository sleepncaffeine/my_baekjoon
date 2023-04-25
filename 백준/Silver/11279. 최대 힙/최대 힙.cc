#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    priority_queue<int> pri_q;
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        if(x==0)
        {
            if(pri_q.empty())
                cout<<0<<"\n";
            else
            {
                cout<<pri_q.top()<<"\n";
                pri_q.pop();
            }
        }
        else
            pri_q.push(x);
    }
    return 0;
}
