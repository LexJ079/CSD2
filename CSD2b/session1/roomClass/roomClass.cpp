#include <iostream>
#include <string>

class Room{
	public:
		std::string name;
		int chairs;
		bool desk;
		bool bed;

		void scanChairs()
		{
			std::cout << name << " has " << chairs << " chairs. " << std::endl;
		}



void hasDesk(){
if(desk){
	std::cout << "There is a desk" << std::endl;
	}

}

void hasBed(){
if(bed){
	std::cout << "There is a bed" <<std::endl;

}

}
};

int main()
{
	Room Room1;
	Room1.name = "bedroom";
	Room1.chairs = 3;
	Room1.desk = true;
	Room1.bed = true;

	Room1.scanChairs();
	Room1.hasDesk();
	Room1.hasBed();

	return 0;

};
