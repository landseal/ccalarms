// compile with gcc -o program alarmreader.c -lwiringPi
// run with ./program

#include <stdio.h>
#include <wiringPi.h>

#define led 7

int main()
{
	printf("Hello world \n");

	wiringPiSetup();

	pinMode(led, OUTPUT);

	while(1) {
		printf("on \n");
		digitalWrite(led, HIGH);
		delay(1000);
		printf("off \n");
		digitalWrite(led, LOW);
		delay(1000);
	}
	return 0;
}
