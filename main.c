#include <REGX52.H>
#include "LCD1602.h"

void main()
{
	DS1302_Init();
	DS1302_setTime();
	while(1)
	{
		DS1302_readTime();
	}
}