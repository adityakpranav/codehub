#include<stdio.h>
char* numberIsPositiveOrNegativeOrZero(int num);
void main(){
	int num;
	scanf("%d",&num);
	printf(numberIsPositiveOrNegativeOrZero(num));
	}
char* numberIsPositiveOrNegativeOrZero(int num){
	return((num>=0)?((num==0)?"Zero":"Positive"):"Negative");
}
