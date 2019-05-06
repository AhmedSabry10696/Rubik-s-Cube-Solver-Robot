#define right portb.b0
#define down portb.b1
#define left portb.b2
#define back portb.b3
#define front portb.b4
#define up portb.b5

#define enable portc.b0
#define dir portc.b1
#define clk portc.b2

#define on 1
#define off 0
#define delay 40

unsigned long i;

void rotate_90(void)
{
 dir=0;
 delay_ms(5);

 for(i=0;i<400;i++)
 {
   clk=on;
   delay_us(50);
   clk=off;
   delay_us(50);
 }
 portb=0x00;
}

void rotate_180(void)  // function to rotate 180 degree with clock wise
{
 dir=0;
 delay_ms(5);
 for(i=0;i<800;i++)   // i <800  --> 180 degree
 {
   clk=on;
   delay_us(50);
   clk=off;
   delay_us(50);
 }
  portb=0x00;
}

void rotate_270(void)  // function to rotate 90 degree with anti clock wise
{
 dir=1;
 delay_ms(5);
 for(i=0;i<400;i++)    // i <800  --> 180 degree
 {
   clk=on;
   delay_us(50);
   clk=off;
   delay_us(50);
 }
 portb=0x00;
}

void main(){

volatile unsigned char check;
unsigned char j=0;
unsigned char solve[30];
unsigned char rand[30];

trisb=0x00;
portb=0x00;

trisc.b0 = 0;
trisc.b1 = 0;
trisc.b2 = 0;

portc.b0 = 0;
portc.b1 = 0;
portc.b2 = 0;

uart1_init(9600);
Delay_ms(100);

do
     {
     while(!uart1_data_ready()){}
     uart1_read_text(solve,"ok",30);
     uart1_write_text("solve = ");
     uart1_write_text(solve);
     while(!uart1_data_ready());
     check = uart1_read();
}while(check != '1');

do
{
     while(!uart1_data_ready());
     uart1_read_text(rand,"ok",30);
     uart1_write_text("rand = ");
     uart1_write_text(rand);
     while(!uart1_data_ready());
     check = uart1_read();
}while(check != '1');

while(1)
{

if(uart1_data_ready())
{
check = uart1_read();
if(check == 's')
{
j = 0;
while(solve[j]!= '\0')
{
    switch(solve[j])
    {
     case 'R':
            {
             right=on;
             delay_ms(delay);
             rotate_90();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'r':
            {
             right=on;
             delay_ms(delay);
             rotate_270();
             portb=0x00;
             delay_ms(delay);
            }break;
     case '0':
            {
             right=on;
             delay_ms(delay);
             rotate_180();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'D':
            {
             down=on;
             delay_ms(delay);
             rotate_90();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'd':
            {
             down=1;
             delay_ms(delay);
             rotate_270();
             portb=0x00;
             delay_ms(delay);
            }break;
     case '1':
            {
             down=1;
             delay_ms(delay);
             rotate_180();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'L':
            {
             left=1;
             delay_ms(delay);
             rotate_90();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'l':
            {
             left=1;
             delay_ms(delay);
             rotate_270();
             portb=0x00;
             delay_ms(delay);
            }break;
     case '2':
            {
             left=1;
             delay_ms(delay);
             rotate_180();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'B':
            {
             back=1;
             delay_ms(delay);
             rotate_90();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'b':
            {
             back=1;
             delay_ms(delay);
             rotate_270();
             portb=0x00;
             delay_ms(delay);
            }break;
     case '3':
            {
             back=1;
             delay_ms(delay);
             rotate_180();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'F':
            {
             front=1;
             delay_ms(delay);
             rotate_90();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'f':
            {
             front=1;
             delay_ms(delay);
             rotate_270();
             portb=0x00;
             delay_ms(delay);
            }break;
     case '4':
            {
             front=1;
             delay_ms(delay);
             rotate_180();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'U':
            {
             up=1;
             delay_ms(delay);
             rotate_90();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'u':
            {
             up=1;
             delay_ms(delay);
             rotate_270();
             portb=0x00;
             delay_ms(delay);
            }break;
     case '5':
            {
             up=1;
             delay_ms(delay);
             rotate_180();
             portb=0x00;
             delay_ms(delay);
            }break;
    }
   j++;
}
}

else if(check == 'r')
{
j = 0;
while(rand[j]!= '\0')
{
    switch(rand[j])
    {
     case 'R':
            {
             right=on;
             delay_ms(delay);
             rotate_90();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'r':
            {
             right=on;
             delay_ms(delay);
             rotate_270();
             portb=0x00;
             delay_ms(delay);
            }break;
     case '0':
            {
             right=on;
             delay_ms(delay);
             rotate_180();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'D':
            {
             down=on;
             delay_ms(delay);
             rotate_90();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'd':
            {
             down=1;
             delay_ms(delay);
             rotate_270();
             portb=0x00;
             delay_ms(delay);
            }break;
     case '1':
            {
             down=1;
             delay_ms(delay);
             rotate_180();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'L':
            {
             left=1;
             delay_ms(delay);
             rotate_90();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'l':
            {
             left=1;
             delay_ms(delay);
             rotate_270();
             portb=0x00;
             delay_ms(delay);
            }break;
     case '2':
            {
             left=1;
             delay_ms(delay);
             rotate_180();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'B':
            {
             back=1;
             delay_ms(delay);
             rotate_90();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'b':
            {
             back=1;
             delay_ms(delay);
             rotate_270();
             portb=0x00;
             delay_ms(delay);
            }break;
     case '3':
            {
             back=1;
             delay_ms(delay);
             rotate_180();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'F':
            {
             front=1;
             delay_ms(delay);
             rotate_90();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'f':
            {
             front=1;
             delay_ms(delay);
             rotate_270();
             portb=0x00;
             delay_ms(delay);
            }break;
     case '4':
            {
             front=1;
             delay_ms(delay);
             rotate_180();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'U':
            {
             up=1;
             delay_ms(delay);
             rotate_90();
             portb=0x00;
             delay_ms(delay);
            }break;
     case 'u':
            {
             up=1;
             delay_ms(delay);
             rotate_270();
             portb=0x00;
             delay_ms(delay);
            }break;
     case '5':
            {
             up=1;
             delay_ms(delay);
             rotate_180();
             portb=0x00;
             delay_ms(delay);
            }break;
    }
   j++;
}
}

}
}
}