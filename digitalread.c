// compile with gcc -o program alarmreader.c -lwiringPi
// run with ./program

#include <stdio.h>
#include <wiringPi.h>

#define read 7

int main()
{
	printf("Hello world \n");

	wiringPiSetup();
	pinMode(read, INPUT);
	pullUpDnControl(read, PUD_UP);

	while(1) {
		int x = digitalRead(read);
		if(x == 1) {
			printf("hi \n");
		} else {
			printf("lo \n");
		}
		delay(1000);
	}
	return 0;
}
