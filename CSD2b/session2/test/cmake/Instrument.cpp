#include "Instrument.h"
#include <iostream>

void Instrument::play()
{
    std::cout << name << " sounds like " << sound << std::endl;
}

