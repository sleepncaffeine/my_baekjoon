#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    stack<int> s;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        string str;
        cin>>str;
        if(str=="push")
        {
            int dat;
            cin>>dat;
            s.push(dat);
        }
        else if(str=="pop")
        {
            if(!s.empty())
            {
                cout<<s.top()<<"\n";
                s.pop();
            }
            else
                cout<<"-1\n";
        }
        else if(str=="size")
            cout<<s.size()<<"\n";
        else if(str=="empty")
        {
            if(s.empty())
                cout<<"1\n";
            else
                cout<<"0\n";
        }
        else if(str=="top")
        {
            if(!s.empty())
                cout<<s.top()<<"\n";
            else
                cout<<"-1\n";
        }
    }
    return 0;
}
