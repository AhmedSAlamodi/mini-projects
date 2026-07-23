#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int num1;
    char op;
    int num2;

    // Welcome to smart Calculator
    printf("Welcome to the smart calculator \n");

    // Enter Number1
    num1 = get_int("Enter Number1: ");

    // Enter the Calculator Operator
    op = get_char("Enter the Calculator Operator?: ");

    // Enter Number2
    num2 = get_int("Enter Number2: ");

    // Calculator Operator
    if (op == '+')
    {
        printf("%i + %i = %i\n", num1, num2, num1 + num2);
    }
    else if (op == '-')
    {
        printf("%i - %i = %i\n", num1, num2, num1 - num2);
    }
    else if (op == '*')
    {
        printf("%i * %i = %i\n", num1, num2, num1 * num2);
    }
    else if (op == '/')
    {
        printf("%i / %i =%i\n", num1, num2, num1 / num2);
    }

}
