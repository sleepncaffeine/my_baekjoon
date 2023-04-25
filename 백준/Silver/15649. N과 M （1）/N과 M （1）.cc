#include <bits/stdc++.h>
using namespace std;

int n,m;
int arr[9]={0,};
int visited[9]={0,};

void dfs(int k)
{
    if(k==m)
    {
        for(int i=0;i<m;i++)
            printf("%d ",arr[i]);
        printf("\n");
    }
    else
    {
        for(int i=1;i<=n;i++)
        {
            if(visited[i]==0)
            {
                visited[i]=1;
                arr[k]=i;
                dfs(k+1);
                visited[i]=0;
            }
        }
    }
}

int main()
{
    scanf("%d %d",&n,&m);
    dfs(0);
}
