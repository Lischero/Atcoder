#include <stdio.h>
#include <stdlib.h>
#define factor ((unsigned long int)1e5)

typedef struct{
	unsigned long int a;
	unsigned long int f;
}array;

/*以下比較関数。*/
int comp(const void *c1, const void *c2){
	array test1 = *(array *)c1;
	array test2 = *(array *)c2;
	int tmp1 = test1.a;
	int tmp2 = test2.a;
	return tmp1 - tmp2;
}

int main (void){
	unsigned int N = 1;
	unsigned long int a[factor] = {0};
	scanf("%d",&N);
	array s[N];
	unsigned long int c,v,m,ans = 0;
	for(c = 0; c < N; c++){
		scanf("%ld",&a[c]);
		s[c].a = a[c];
		s[c].f = c;
	}
	qsort(s,N,sizeof(array),comp);
	for(c = 0; c < N; c = v){
		v = c+1;
		while ((v < N) && (s[c].a == s[v].a)) v++;
		for(m = c; m < v; a[(s[m++].f)] = ans);
		ans++;
	}
	for(c = 0; c < N; c++) printf("%ld\n",a[c]);
	return 0;
}
