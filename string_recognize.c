#include <stdio.h>
#include<string.h>
#include<conio.h>
#include<stdlib.h>

void main()
{
    char s[20],c;
    int state=0,i=0;
    printf("Enter a string:\n");
    gets(s);
    while(s[i]!='\0')
    {
        switch(state)
        {
        case 0: c=s[i++];
            if(c=='a')
                state=1;
            else if(c=='b')
                state=2;
            else
                state=6;
            break;
        case 1: c=s[i++];
            if(c=='a')
                state=3;
            else if(c=='b')
                state=4;
            else
                state=6;
            break;
        case 2: c=s[i++];
            if(c=='a')
                state=6;
            else if(c=='b')
                state=2;
            else
                state=6;
            break;
        case 3: c=s[i++];
            if(c=='a')
                state=3;
            else if(c=='b')
                state=2;
            else
                state=6;
            break;
        case 4: c=s[i++];
            if(c=='a')
                state=6;
            else if(c=='b')
                state=5;
            else
                state=6;
            break;
        case 5: c=s[i++];
            if(c=='a')
                state=6;
            else if(c=='b')
                state=2;
            else
                state=6;
            break;
        case 6: printf("not recognised under any production",s);
        exit(0);
        }
    }
    if(state==3)
    printf("produced by 'a*'\n");
    else if((state==2)||(state==4))
    printf("produced by 'a*b+'\n");
    else if(state==5)
    printf("produced by 'abb'\n");
}