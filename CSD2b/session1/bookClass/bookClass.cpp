#include <iostream>
#include <string>

class book{
	public:
		std::string title;
		std::string author;
		std::string category;

		int pages;
		int year;

		bool introduction;
		bool images;

		float weight;

		void description(){

			std::cout << "The title of this book is " << title << ", it is written by " << author << ", and it belongs to the category of: " << category << ". " << std::endl;

			std::cout << "It counts " << pages << " pages, " << "and this version was first published in: " << year << ". " << "It weighs around " << weight << "kg. " << std::endl;

			if(introduction){
				std::cout << title << " has an introduction before the book starts." << std::endl;
			}

			if(images){
				std::cout << "The book contains images." << std::endl;
			}
			else
			{
				std::cout << "The book contains no images." << std::endl;
			}
		}

	

};

int main(){

	book book1;
	book1.title = "The Hobbit";
	book1.author = "J.R.R. Tolkien";
	book1.category = "Fantasy";
	book1.pages = 320;
	book1.year = 2020;
	book1.introduction = false;
	book1.images = true;
	book1.weight = 0.79f;


	book book2;
	book2.title = "1984";
	book2.author = "G. Orwell";
	book2.category = "Dystopian Fiction";
	book2.pages = 336;
	book2.year = 2009;
	book2.introduction = true;
	book2.images = false;
	book2.weight = 0.19f;


	book book3;
	book3.title = "The Bible";
	book3.author = "The Prophets and Saints";
	book3.category = "Truth";
	book3.pages = 1984;
	book3.year = 2008;
	book3.introduction = true;
	book3.weight = 1.42f;

	book1.description();
	book2.description();
	book3.description();

	return 0;
};
