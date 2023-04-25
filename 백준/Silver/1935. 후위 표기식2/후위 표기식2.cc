#include <bits/stdc++.h>
using namespace std;

int alph[26];
int n;
string str;
stack<double>s;

int main()
{
    cin>>n;
    cin>>str;
    for(int i=0;i<n;i++)
        cin>>alph[i];
    for(int i=0;i<str.length();i++)
    {
        if(!isalpha(str[i]))
        {
            double x=s.top();
            s.pop();
            double y=s.top();
            s.pop();
            if(str[i]=='+')
                s.push(x+y);
            else if(str[i]=='-')
                s.push(y-x);
            else if(str[i]=='*')
                s.push(x*y);
            else if(str[i]=='/')
                s.push(y/x);
        }
        else
            s.push(alph[str[i]-'A']);
    }
    double res=s.top();
    cout<<fixed;
    cout.precision(2);
    cout<<res;
    return 0;
}
