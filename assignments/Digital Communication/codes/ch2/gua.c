#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

#define GAUSSIAN_DATA_PATH	"../data/gau.dat"

int  main(void) //main function begins
{
 
//Gaussian random numbers
gaussian(GAUSSIAN_DATA_PATH, 1000000);

//Mean and variance of Gaussian
printf("Mean: %lf\n",mean(GAUSSIAN_DATA_PATH));
printf("Variance: %lf\n",variance(GAUSSIAN_DATA_PATH));
return 0;
}
