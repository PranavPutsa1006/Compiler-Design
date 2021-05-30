#include <stdio.h>
void main()
{
    char s[50];
    printf("Enter text:\n");
    gets(s);
    int c=0;
    if(s[0]=='/' && s[1]=='*')
    {
        for(int i=2;i<48;i++)
            {
                if(s[i]=='*' && s[i+1]=='/')
                    {
                        c=1;
                        break;
                    }
                else
                    continue;
            }
            if(c==0)
                printf("Not a Comment\n");
            else
                printf("Comment\n");
    }
    else
    {
        printf("Not a Comment\n");
    }
}
