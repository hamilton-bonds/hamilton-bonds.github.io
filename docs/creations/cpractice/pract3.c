#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int checkValue(int randNum, int *guesses) {
	int i;
	for(i=0;i<5;i++) {
		if(guesses[i]==randNum) {
			return 1;
		}
	}
	return 0;
}

int main() {
	int *p_tries, tries;
	p_tries = &tries;
	int *p_randNum, randNum;
	p_randNum = &randNum;
	int *p_highNum, highNum;
	p_highNum = &highNum;
	int *p_lowNum, lowNum;
	p_lowNum = &lowNum;
	int *p_guessed, guessed;
	p_guessed = &guessed;
	int* p_userResponse;
	char userResponse[1];
	//p_userResponse = &userResponse;
	int *p_prevGuess, prevGuess;
	p_prevGuess = &prevGuess;
	int guesses[5];

	tries = 0;
	randNum = 0;
	highNum = 100;
	lowNum = 1;
	guessed = 0;
	srand(time(0));

	printf("Think of a number between 1 and 100\n\n");

	while(tries<=5 && guessed==0) {
		prevGuess = *p_randNum;
		while(prevGuess==*p_randNum || checkValue(randNum,guesses)==1) {
			*p_randNum = rand() % (highNum + 1 - lowNum) + lowNum;
		}
		if((highNum-lowNum)==2) {
			randNum = highNum-1;
		}
		printf("\n---------------------------------------------------\n");
		printf("Computer Guess #%i: %i\n\n",tries,randNum);

		printf("\nIs %i [h]igher, [l]ower, or [e]xactly your number?\n",randNum);
		scanf("%s",userResponse);
		printf("\n\tUser Response: \t%s\n",userResponse);

		if (*userResponse=='h') {
			*p_highNum = randNum;
		}
		else if(*userResponse=='l') {
			*p_lowNum = randNum;
		}
		else if(*userResponse=='e') {
			*p_guessed = 1;
		}
		else {
			printf("ERROR!\n");
		}

		printf("\tHighest: \t%i\n",highNum);
		printf("\tLowest: \t%i\n",lowNum);
		printf("\n---------------------------------------------------\n");

		guesses[tries] = randNum;
		tries++;
	}
	if(tries>=6 && guessed==0) { //One last guess
		prevGuess = *p_randNum;
		while(prevGuess==*p_randNum || checkValue(randNum,guesses)==1) {
			*p_randNum = rand() % (highNum + 1 - lowNum) + lowNum;
		}
		if((highNum-lowNum)==2) {
			randNum = highNum-1;
		}
	}
	printf("Is this your number: %i?\n\n",randNum);
	return 0;
}
