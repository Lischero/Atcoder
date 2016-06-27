#include <stdio.h>
#include <stdlib.h>
int sorting(const void *a, const void *b){
	if(*(int*)a < *(int*)b){
		return -1;
	} else if(*(int*)a == *(int*)b){
		return 0;
	}
	return 1;
}
		
int main(){
	int i=0,f=0,numbers[6],result[10];
	scanf("%d %d %d %d %d",&numbers[0],&numbers[1],&numbers[2],&numbers[3],&numbers[4]);
	for(i=0;i<3;i++){
		for(int j=i+1;j<4;j++){
			for(int z=j+1;z<5;z++){
					result[f]=numbers[i]+numbers[j]+numbers[z];
					f++;
			}
		}
	}
	qsort(result,10,sizeof(int),sorting);
	printf("%d\n",result[7]);
	return 0;
}
