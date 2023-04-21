#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
char arr[3072][6143];

void draw(int r,int c)
{
    arr[r][c]='*';
    arr[r+1][c-1]='*';
    arr[r+1][c+1]='*';
    for(int i=0;i<5;i++)
        arr[r+2][c+i-2]='*';
}

void tri(int l,int r,int c)
{
    if(l==3)
    {
        draw(r,c);
        return;
    }
    tri(l/2,r,c);
    tri(l/2,r+l/2,c-l/2);
    tri(l/2,r+l/2,c+l/2);
}
int main()
{
    cin >> n;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<2*n-1;j++)
        {
            arr[i][j]=' ';
        }
    }
    tri(n,0,n-1);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<2*n-1;j++)
        {
            cout<<arr[i][j];
        }
        cout<<'\n';
    }
    return 0;
}
