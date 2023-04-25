#include <bits/stdc++.h>
using namespace std;

double a,b,c,x=0,px;

int main()
{
    cin>>a>>b>>c;
    while(fabs(a*x + b*sin(x) - c)>0.00000001)
    {
        px=x-(a*x + b*sin(x) - c)/(a + b*cos(x));
        x=px;
    }
    cout<<fixed;
    cout.precision(9);
    cout<<x;
    return 0;
}
