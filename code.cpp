#include <iostream>
#include <string>
using namespace std;
class nameRecordClass{
	public:
		void setName(string x){
		name = x;
		}
		string getName(){
			return name;
		}
	private:
		string name;
};

int main() {
	nameRecordClass someObject;
	someObject.setName("asdf");
	cout << someObject.getName() << endl;
	cout << "Code and stuff" << endl;
	


	for (int =0; i < 10; ++i) {

		cout << "Wow what a loop!" << endl;
	}
	// Another comment!
	// Soft reset does what?
	return 0;
}
