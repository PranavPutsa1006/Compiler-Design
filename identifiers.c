#include <stdio.h>
#include <string.h>
void main()
{
    char s[20];
    printf("Enter text:\n");
    gets(s);
    int c=1;
    if((s[0]>='a' && s[0]<='z')||(s[0]>='A' && s[0]<='Z')||s[0]=='_')
    {
        for(int i=1;i<strlen(s);i++)
            {
                if((s[i]>='a' && s[i]<='z')||(s[i]>='A' && s[i]<='Z')||(s[i]>='0' && s[i]<='9')||s[i]=='_'||s[i]=='\n')
                    {
                        continue;
                    }
                else
                {
                    c=0;
                    break;
                }
            }
            if(c==0)
                printf("Not an Identifier\n");
            else
                printf("An Identifier\n");
    }
    else
    {
        printf("Not an Identifier\n");
    }
}
