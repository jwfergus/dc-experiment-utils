#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <time.h>


void *foreverCPULoop(void *arg)
{

	/*
	 *	Using random numbers tasks both FPU instruction branching
	 */
	char *str;
	str=(char*)arg;
	printf("inside CPU loop");
	while(1)
	{
		srand(time(NULL));
		float i = 99.9 * 99.9;
		int j = 99 * rand();
		if(i>j){
		float i = 88.8 * rand();
		}
	}

	return NULL;
}

void *foreverHDDLoop(void *arg)
{
	/*
	 *	Writes random numbers to 10,000 character file. Randomly chooses
	 *	 a location under index 5000 to read 5000 characters forward on
	 */

	while(1)
	{
		printf("inside HDD loop");
		FILE *file; 
		file = fopen("taskHDDFile","w"); 
		int iterator;
		srand(time(NULL));
		for ( iterator = 0; iterator < 10000; iterator++ ) 
		{
			fprintf(file,"%d",rand());  
		}
		fclose(file); 
	
		char buffer[sizeof(int)*10000];
		if (file = fopen("taskHDDFile", "r+"))
		{
			for ( iterator = 0; iterator < 5; iterator++ ) 
			{
				int random_number = rand() %5000;
				fread(buffer, 1, (random_number+5000), file);
			}
			fclose(file);

		}
	}

	return NULL;
}

void *foreverMemLoop(void *arg)
{

	
	/*
	 *	Creates large Matrix. Matrices are stored in memory as row1,row2,...rowN
	 *	 thus accessing column 1 of row1,row2,row3, etc. causes cache miss at each
	 *	 access
	 */
	srand(time(NULL));
	while(1)
	{
	printf("inside Mem loop");
		int temp_array[1024][1024];
		int column, row;
		for(column=0; column<=1023; column++)
		{
			for(row=0; row<=1023; row++)
			{
				temp_array[row][column] = rand();
			}
		}
	}
	return NULL;

}

int main(int argc, char *argv[])
{
	pthread_t pth1, pth2, pth3, pth4, pth5, pth6;

	pthread_create(&pth1,NULL,foreverCPULoop,"processing...");
	pthread_create(&pth2,NULL,foreverCPULoop,"processing...");
	pthread_create(&pth3,NULL,foreverCPULoop,"processing...");
	pthread_create(&pth4,NULL,foreverCPULoop,"processing...");


	pthread_join(pth1, NULL );
	pthread_join(pth2, NULL );
	pthread_join(pth3, NULL );
	pthread_join(pth4, NULL );

	return 0;
}
