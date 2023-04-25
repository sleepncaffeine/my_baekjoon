#include <bits/stdc++.h>
#include <string>
using namespace std;

int main()
{
    int n;
    deque<int> d;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        string str;
        cin>>str;
        if(str=="push_front")
        {
            int n;
            cin>>n;
            d.push_front(n);
        }
        else if(str=="push_back")
        {
            int n;
            cin>>n;
            d.push_back(n);
        }
        else if(str=="pop_front")
        {
            if(d.empty())
                cout<<"-1\n";
            else
            {
                cout<<d.front()<<"\n";
                d.pop_front();
            }
        }
        else if(str=="pop_back")
        {
            if(d.empty())
                cout<<"-1\n";
            else
            {
                cout<<d.back()<<"\n";
                d.pop_back();
            }
        }
        else if(str=="size")
            cout<<d.size()<<"\n";
        else if(str=="empty")
            cout<<d.empty()<<"\n";
        else if(str=="front")
        {
            if(d.empty())
                cout<<"-1\n";
            else
                cout<<d.front()<<"\n";
        }
        else if(str=="back")
        {
            if(d.empty())
                cout<<"-1\n";
            else
                cout<<d.back()<<"\n";
        }
    }
    return 0;
}
