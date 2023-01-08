#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

#define UNIFORM_DATA_PATH	"../data/uni.dat"

int  main(void) //main function begins
{
 
//Uniform random numbers
uniform(UNIFORM_DATA_PATH, 1000000);

//Mean and variance of Uniform
printf("Mean: %lf\n",mean(UNIFORM_DATA_PATH));
printf("Variance: %lf\n",variance(UNIFORM_DATA_PATH));
return 0;
}
