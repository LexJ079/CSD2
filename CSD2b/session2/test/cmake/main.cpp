#include "Instrument.h"

int main()
{
    Instrument instrument1;
    instrument1.name = "cymbal";
    instrument1.sound = "Tsssss";

    Instrument instrument2;
    instrument2.name = "triangle";
    instrument2.sound = "ding";

    instrument1.play();
    instrument2.play();

    return 0;
}

