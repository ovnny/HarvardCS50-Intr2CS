#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long cardN,rem1,sum1 = 0;
    long rem2,sum2 = 0;
    long checkSum = 0;
        
    cardN = get_long("Number: ");
    long cardN1=cardN;
    long cardN2=cardN;
    
    while (cardN1 > 0 && cardN2 > 0)
    {
        rem1 = (cardN1%100)/10;
        sum1 += (rem1*2)%10;
        cardN1 = cardN1 / 100; 
        if(rem1 >= 5)
        {
            sum1++;  
        }       
                
        rem2 = (cardN2%100)%10;
        sum2 = (rem2 + sum2);
        cardN2 = (cardN2 / 100);
    }

    checkSum = sum1 + sum2;

    //American Express uses 15-digit numbers, start with 34 or 37
    //MasterCard uses 16-digit numbers, start with 51, 52, 53, 54, or 55
    //Visa uses 13- and 16-digit numbers, start with 4

    if (checkSum%10 == 0)
    {
        if ((cardN >= 34*pow(10,13) && cardN <= 35*pow(10,13)-1) ||
        (cardN >= 37*pow(10,13) && cardN <= 38*pow(10,13) -1))
        {
            printf("AMEX\n");
        }
        else if ((cardN >= 51*pow(10,14)) && (cardN <= 56*pow(10,14) -1))
        {
            printf("MASTERCARD\n");
        }
        else if ((cardN >= 4*pow(10,13) && cardN <= 5*pow(10,13)-1) ||
        (cardN >= 4*pow(10,15) && cardN < 5*pow(10,15)))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
}