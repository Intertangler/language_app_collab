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

	// Soft reset does what?
	return 0;
}
