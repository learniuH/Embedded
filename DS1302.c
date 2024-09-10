#include <REGX52.H>

sbit DS1302_CE   = P3^5;
sbit DS1302_IO   = P3^6;
sbit DS1302_SCLK = P3^7;

#define DS1302_Seconds 0x80
#define DS1302_Minutes 0x82
#define DS1302_Hour	   0x84
#define DS1302_Date    0x86
#define DS1302_Month   0x88
#define DS1302_Year    0x8C
#define DS1302_WP	   0x8E

unsigned char DS1302_TIME[] = {24, 9, 10, 20, 55, 55};	//�꣬�£��գ�ʱ���֣���

void DS1302_Init()
{
	DS1302_CE = 0;
	DS1302_SCLK = 0;
}

void DS1302_writeByte(unsigned char command, Data)
{
	unsigned char i;
	DS1302_CE = 1;
	//��ȡ����
	for(i = 0; i < 8; i++)
	{
		DS1302_IO = command & (0x01 << i);
		DS1302_SCLK = 1;
		DS1302_SCLK = 0;
	}
	//��������
	for(i = 0; i < 8; i++)
	{
		DS1302_IO = Data & (0x01 << i);
		DS1302_SCLK = 1;
		DS1302_SCLK = 0;
	}
	DS1302_CE = 0;
}

unsigned char DS1302_readByte(unsigned char command)
{
	unsigned char i, Data = 0x00;
	command |= 0x01;	//������ת��Ϊ������
	DS1302_CE = 1;
	//��ȡ����
	for(i = 0; i < 8; i++)
	{
		DS1302_IO = command & (0x01 << i);
		DS1302_SCLK = 0;
		DS1302_SCLK = 1;
	}
	//��ȡ����
	for(i = 0; i < 8; i++)
	{
		
		
		DS1302_SCLK = 1;
		DS1302_SCLK = 0;
		
		
		if(DS1302_IO)	//�����ʱIO������Ϊ1
		{
			Data |= 0x01 << i;
		}
	}
	DS1302_CE = 0;
						//DS1302_IO = 0;	//��ȡ��IO��0������ᱨ��
	return Data;
}


//�� DS1302 ��BCDʱ��ת����ʮ����ʱ��
unsigned char DS1302_BCD_TO_DEC(unsigned char Data)
{
	unsigned ret;
	ret = Data / 16 * 10 + Data % 16;
	return ret;
}


//��ʮ���Ƶ�ʱ�䣬ת��Ϊ DS1302 ��BCDʱ��
unsigned char DS1302_DEC_TO_BCD(unsigned char Data)
{
	unsigned char ret;
	ret = Data / 10 * 16 + Data % 10;
	return ret;
}

void DS1302_setTime()
{
	DS1302_writeByte(DS1302_WP,      0x00);	//ȡ��д����
	DS1302_writeByte(DS1302_Year,    DS1302_DEC_TO_BCD(DS1302_TIME[0]));
	DS1302_writeByte(DS1302_Month,   DS1302_DEC_TO_BCD(DS1302_TIME[1]));
	DS1302_writeByte(DS1302_Date,     DS1302_DEC_TO_BCD(DS1302_TIME[2]));
	DS1302_writeByte(DS1302_Hour,    DS1302_DEC_TO_BCD(DS1302_TIME[3]));
	DS1302_writeByte(DS1302_Minutes, DS1302_DEC_TO_BCD(DS1302_TIME[4]));
	DS1302_writeByte(DS1302_Seconds, DS1302_DEC_TO_BCD(DS1302_TIME[5]));
	DS1302_writeByte(DS1302_WP,      0x80); //д����
}

void DS1302_readTime()
{
	DS1302_TIME[0] = DS1302_BCD_TO_DEC(DS1302_readByte(DS1302_Year));
	DS1302_TIME[1] = DS1302_BCD_TO_DEC(DS1302_readByte(DS1302_Month));
	DS1302_TIME[2] = DS1302_BCD_TO_DEC(DS1302_readByte(DS1302_Date));
	DS1302_TIME[3] = DS1302_BCD_TO_DEC(DS1302_readByte(DS1302_Hour));
	DS1302_TIME[4] = DS1302_BCD_TO_DEC(DS1302_readByte(DS1302_Minutes));
	DS1302_TIME[5] = DS1302_BCD_TO_DEC(DS1302_readByte(DS1302_Seconds));
}