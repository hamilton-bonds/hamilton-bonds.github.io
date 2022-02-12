#include <stdio.h>
#include <math.h>

//This is a comment
int main() {
	int age;
	int* p_age;
	int mhr;
	int* p_mhr;
	p_age = &age;
	p_mhr = &mhr;

	printf ("What is your age?");
	scanf ("%i", *p_age);
	mhr = 220-*p_age;
	printf ("Your max recommended heart rate is %i",*p_mhr);
	return 0;
}
