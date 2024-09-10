#ifndef __DS1302_H__
#define __DS1302_H__

extern unsigned char DS1302_TIME[];

void DS1302_Init();
void DS1302_writeByte(unsigned char command, Data);
unsigned char DS1302_readByte(unsigned char command);
void DS1302_setTime();
void DS1302_readTime();

#endif