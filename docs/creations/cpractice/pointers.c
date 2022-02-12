#include <stdio.h>

int test(int *var) {
	*var -= 5;
}

int main() {
	int *p_var, var;
	p_var = &var;
	var = 100;
	printf("\n%i\n",p_var);
	printf("\n%i\n",var);
	while(var>0) {
		test(&var);
		printf("\n%i\n",p_var);
		printf("\n%i\n",var);
	}
	printf("Done...\n");
}
