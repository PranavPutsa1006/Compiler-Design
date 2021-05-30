#include <stdio.h>
void main()
{
    char s[50];
    printf("Enter text:\n");
    gets(s);
    if(s[0]=='/')
    {
        if(s[1]=='/')
            printf("Comment\n");
    }
     else if(s[0]!='/')
     {
         for(int i=0;i<46;i++)
        {
            if(s[i]==' ')
            {
                continue;
            }
            else if(s[i]=='/')
            {
                if(s[i+1]=='/')
                    printf("Comment\n");
            }
        }
     }
     else
     {
         printf("Not a comment\n");
     }
}
