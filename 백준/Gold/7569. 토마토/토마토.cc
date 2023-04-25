#include <bits/stdc++.h>
using namespace std;

int tmt[100][100][100];
int m,n,h;
int dxyz[6][3]={{0,0,1},{0,1,0},{1,0,0},{-1,0,0},{0,-1,0},{0,0,-1}};
struct coord
{
    int x,y,z;
};
queue<coord> T;


int main()
{
    //input
    scanf("%d %d %d",&n,&m,&h);
    for(int i=0;i<h;i++)
    {
        for(int j=0;j<m;j++)
        {
            for(int k=0;k<n;k++)
            {
                scanf("%d",&tmt[k][j][i]);
                if(tmt[k][j][i]==1)
                {
                    T.push({k,j,i});
                }
            }
        }
    }

    //bfs
    int day=2;
    while(!T.empty())
    {
        int cycle=T.size();
        for(int i=0;i<cycle;i++)
        {
            int a=T.front().x,b=T.front().y,c=T.front().z;
            T.pop();
            for(int j=0;j<6;j++)
            {
                int da=a+dxyz[j][0],db=b+dxyz[j][1],dc=c+dxyz[j][2];
                if(da>=n||db>=m||dc>=h||da<0||db<0||dc<0||tmt[da][db][dc]!=0)
                    continue;
                tmt[da][db][dc]=day;
                T.push({da,db,dc});
            }
        }
        day++;
    }

    //output
    int res=0,flag=0;
    for(int i=0;i<h;i++)
    {
        for(int j=0;j<m;j++)
        {
            for(int k=0;k<n;k++)
            {
                if(tmt[k][j][i]==0)
                {
                    res=0;
                    flag=1;
                    break;
                }
                if(res<tmt[k][j][i])
                    res=tmt[k][j][i];
            }
            if(flag) break;
        }
        if(flag) break;
    }

    printf("%d",res-1);

    return 0;
}
