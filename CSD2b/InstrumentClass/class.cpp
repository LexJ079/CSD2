#include <iostream>
#include <string>

class Instrument
{
public:
    std::string name;
    std::string sound;

    void play()
    {
        std::cout << name << " sounds like " << sound << std::endl;
    }
};

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

