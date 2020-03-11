 #include <stdio.h>
#include <string.h>
void main()
{
char opcode[10],mnemonic[10],operand[10],label[10],code[10];
int locctr,start,length,flag=0;
FILE *fp1,*fp2,*fp3,*fp4;
fp1=fopen("INPUT1.txt","r");
fp2=fopen("st.txt","w");
fp3=fopen("out.txt","w");
	fp4=fopen("MOT.txt","r");
fscanf(fp1,"%s%s%s",label,opcode,operand);
printf("%s%s%s",label,opcode,operand);
if(strcmp(opcode,"START")==0)
{
locctr=0;
fprintf(fp3,"%s\t%s\t%s\n",label,opcode,operand);
fscanf(fp1,"%s%s%s",label,opcode,operand);
}
while(strcmp(opcode,"END")!=0)
{
    fprintf(fp3,"%d\t",locctr); 
   if(strcmp(label,"**")!=0)
    fprintf(fp2,"%s\t%d\n",label,locctr);
    
     fscanf(fp4,"%s",mnemonic);
if(strcmp(opcode,"DC")==0)
{
if(operand[0] == 'F')
locctr+=4;
else
locctr+=2;
}
else if(strcmp(opcode,"DS")==0)
{
 if(operand[1] == 'F')
locctr+=4;
else
locctr+=2;
}
   else if(strcmp(opcode,"USING")==0)
   {
   locctr+=0;
      }
while(strcmp(mnemonic,"END")!=0)
    {

    if(strcmp(opcode,mnemonic)==0)
    {
      
           locctr+=4;
flag=1;
           break;
     }
    fscanf(fp4,"%s",mnemonic);
    }


flag=0;
fprintf(fp3,"%s\t%s\t%s\n",label,opcode,operand);
fscanf(fp1,"%s%s%s",label,opcode,operand);
rewind(fp4);
}
fprintf(fp3,"%d\t%s\t%s\t%s\n",locctr,label,opcode,operand);
length=locctr-start;
printf("\n The length of the program is %d",length);
fclose(fp1);
fclose(fp2);
fclose(fp3);
fclose(fp4);
}

