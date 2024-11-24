#import <iostream>

class Classroom{
	public:
	int chairs = 30;
	int desks = chairs / 2;

	bool speakers = false;
		
		Classroom();
		bool haveSpeakers();


};

Classroom::Classroom(){
	std::cout << "We are in a Classroom - the default constructor" << std::endl;
	std::cout << "The amount of chairs is " << chairs << std::endl;
	std::cout << "The amount of desks is " << desks << std::endl;
	
}


bool Classroom::haveSpeakers(){
if(speakers)
{
	std::cout << "There are speakers" << std::endl;
}
else
{
	std::cout << "We have no speakers..." << std::endl;
}
return true;
}

int main(){
		return 0;
		Classroom Classroom1;
		
};
