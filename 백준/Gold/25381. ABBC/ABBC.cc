#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string x;
    cin >> x;

    deque<int> A;
    deque<int> B;

    int ans = 0;
    for (int i = 0; i < x.length(); i++)
    {
        if (x[i] == 'C')
        {
            if (!B.empty() && B.front() < i)
            {
                B.pop_front();
                ans++;
            }
        }
        else if (x[i] == 'B')
            B.push_back(i);
        else if (x[i] == 'A')
            A.push_back(i);
    }

    while (!A.empty() && !B.empty())
    {
        if (A.front() < B.front())
        {
            B.pop_front();
            A.pop_front();
            ans++;
        }
        else B.pop_front();
    }
    
    cout << ans << '\n';
    return 0;
}