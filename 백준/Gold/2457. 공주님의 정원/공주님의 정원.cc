#include <bits/stdc++.h>

using namespace std;

int n,startdate=301,cnt=0;

typedef struct flower
{
    int start,finish;
}flower;

flower flwr[100001];

bool startarrange(flower x,flower y)
{
    if(x.start==y.start)
        return(x.finish>y.finish);
    return(x.start<y.start);
}

int main()
{
    int a,b,c,d;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d %d %d %d",&a,&b,&c,&d);
        flwr[i].start=a*100+b;
        flwr[i].finish=c*100+d;
    }
    sort(flwr,flwr+n,startarrange);
    int maxstart=0;
    int flag=0;
    for(;;){
        flag=0;
        for(int i=0;i<n;i++){
            if(flwr[i].start<=startdate&&flwr[i].finish>startdate){
                if(flwr[i].finish>maxstart)
                    maxstart=flwr[i].finish;
            flag++;
            }
        }
        startdate=maxstart;
        cnt++;
        if(flag==0){
            cnt=0;
            break;
        }
        if(maxstart>1130)
            break;
    }
    printf("%d",cnt);

    return 0;
}