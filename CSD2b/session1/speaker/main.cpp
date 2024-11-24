#include <iostream>

class Tweeter{
public:
  // default constructor
  Tweeter();
  // overloaded constructor
  Tweeter(float diam);
  
  // fields
  float diameter;
  float conePosition;
};

Tweeter::Tweeter() {
  std::cout << "Tweeter - default constructor\n";
  // NOTE: duplicate code alarm!!
  // constructor delegation is a better strategy!

  // in cm
  diameter = 2.5f;
  // number with an f --> indicate it is a float
  conePosition = 0.0f;
}

Tweeter::Tweeter(float diam) {
  std::cout << "Tweeter - constructor with float diam parameter\n";
  // in cm
  diameter = diam;
  // number with an f --> indicate it is a float
  conePosition = 0.0f;
}

class Woofer{
  public:
    Woofer();
    Woofer(float diam);

    float diameter;
    float conePosition;

};

Woofer::Woofer() {
  std::cout << "Woofer - default constructor\n";
  diameter = 4.0f;
  conePosition = 3.0f;


}

Woofer::Woofer(float diam) {
  std::cout << "Woofer - constructor with float diam parameter\n";
  diameter = diam;
  conePosition = 3.0f;

}


class Speaker{
public:
  Speaker();
  Tweeter aTweeter;
  Woofer Woofer1;
};

Speaker::Speaker() {
  std::cout << "Speaker - constructor\n";
  aTweeter.diameter = 2.4;
  std::cout << "The diameter of the tweeter is: "
    << aTweeter.diameter << "\n";

  std::cout << "The diameter of the woofer is: " << Woofer1.diameter << "\n";

}



int main() {
  Speaker aSpeaker;
};

