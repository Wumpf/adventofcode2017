#include <cstdio>
#include <cstdint>
#include <queue>

const uint64_t factorA = 16807;
const uint64_t factorB = 48271;

void partOne()
{
    uint64_t totalCount = 0;
    uint64_t a = 512;//65;
    uint64_t b = 191;//8921;

    for (int i=0; i<40000000; ++i)
    {
        a = (a * factorA) % 2147483647;
        b = (b * factorB) % 2147483647;

        if ((a & 0xFFFF) == (b & 0xFFFF))
            totalCount++;
    }
    printf("result part one: %i\n", totalCount);
}

void partTwo()
{
    uint64_t totalCount = 0;
    uint64_t a = 512;//65;
    uint64_t b = 191;//8921;

    std::queue<uint16_t> valuesA;
    std::queue<uint16_t> valuesB;

    for (int i=0; i<40000000; ++i)
    {
        a = (a * factorA) % 2147483647;
        b = (b * factorB) % 2147483647;

        if (a % 4 == 0)
            valuesA.push((uint16_t)a);
        if (b % 8 == 0)
            valuesB.push((uint16_t)b);

        if(!valuesA.empty() && !valuesB.empty())
        {
            if (valuesA.front() == valuesB.front())
               totalCount++;
            valuesA.pop();
            valuesB.pop();
        }
    }
    printf("result part two: %i\n", totalCount);
}

int main()
{
    partOne();
    partTwo();
}