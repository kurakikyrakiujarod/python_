#include <stdio.h>
int main() {
	int x;
	int n = 0;
	scanf("%d", &x);

	do {
		n++;
		x /= 10;
	} while(x>0);

	printf("%d\n",n);
	printf("1/10 = %d\n",1/10);
	return 0;
}