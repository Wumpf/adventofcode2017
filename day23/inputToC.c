#include <stdio.h>

int main()
{
    long long a = 1;
    long long b = 0;
    long long c = 0;
    //long long g = 0;
    long long h = 0;

    b = 65;
    c = b;
    if (a != 0)
    {
        b *= 100;
        b += 100000;
        c = b;
        c += 17000;
    }
    while (true)
    {
        /*bool f = false;
        long long d = 2;
        do
        {
            long long e = 2;
            do
            {
                if (d * e == b)
                {
                    f = true;
                    break;
                }
                ++e;
            } while (e - b != 0);
            ++d;
        } while (d - b != 0);

        if (f)
            h++;
        */ 

        // Above is a primitive prime number check on b!
        // If something is *not* a prime number, we increment h.
        if (b % 2 == 0)
            h++;
        else
        {
            for(int i = 3; i < b / 2; i+= 2)
            {
                if (b % i == 0)
                {
                    h++;
                    break;
                }
            }
        }

        if(b - c == 0)
            break;
        b+=17;
    }
    
    printf("%i", h);
}
