#include <iostream>

class Note {
public:
	Note();
	int midiNoteValue;
	int velocity;
};

Note::Note() {
	std::cout << "Note - constructor\n";

}
int main() {
	Note aNote;
	std::cout << "aNote.velocity contains: " << aNote.velocity << "\n";

}
