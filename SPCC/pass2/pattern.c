#include<stdio.h>
int main()
{
	int i,j,n;
	printf("enter number of rows:\n");
	scanf(%d,&n);
	
	for(i=1;i<n;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("%d",j);
		}
		printf("\n");
	}
	return 0;
}
		