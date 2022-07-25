/*
 * main.c
 *
 *  Created on: Jun 30, 2022
 *      Author: Wels
 */
#include "main.h"
#include "RCC.h"
#include "SysTick.h"
#include "GPIO.h"
#include "USART.h"
#include "arm_math.h"
#include "arm_const_structs.h"
#include "arm_common_tables.h"

uint32_t my_arm(q7_t resul, char *buffer)
{
	int i;
	float ans = (resul & 0x80)?-1:0;
	for(i=1;i<8;i++)
	{
		if(resul&(0x80>>i)){
			ans+=1.0/(1U<<i);
		}
	}
	return sprintf(buffer,"Resultado q7: 0x%X , decimal = %i y float:%.20f\r\n",resul,resul,ans);
}

q7_t multiplicacion(q7_t a, q7_t b)
{
	q15_t result;
	result = a * b;
	result = result << 1;
	return ((q7_t)(result >> 8));
}

int main(void)
{
	char buffer[250] = {0};
	q7_t a = 0x040;
	q7_t b = 0x23;
	q7_t c;
	uint32_t size;

	Sys_ClockConfig();
	SysTick_ClockConfig(SysTick_ClockMax);
	GPIO_Leds_Init();
	USART_Init(Baudios_115);
	printf("TP1 PSF: Parte 5!\r\n");
	printf("--------------\r\n");
	Delay_ms(1000);
	while(1)
	{
		c = multiplicacion(a, b);
		size = my_arm(c,buffer);
		for (uint32_t i=0; i<size; i++){
			USART_Tx(buffer[i]);
			Delay_ms(100);
		}
		printf("--------------\r\n");
		Delay_ms(1000);
	}
	return 0;
}
