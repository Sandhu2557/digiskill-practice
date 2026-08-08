#include <iostream>
#include <limits>
using namespace std;
class human{
    private:
        string name;
        int age;
        string address;
        public:
        human(string n,int a,string addr){
            name = n;
            age = a;
            address = addr;
        }
        void input(){
            cout<<"Enter your name: ";
            getline(cin,name);
            cout<<"Enter your age: ";
            cin>>age;
            cout<<"Enter your address: ";
            getline(cin,address);
        }
        void display(){
            cout<<"Name: "<<name<<endl;
            cout<<"Age: "<<age<<endl;
            cout<<"Address: "<<address<<endl;
        }
};
int main(){

    human h1("John",25,"New York");
    h1.display();
    h1.input();
    h1.display();
    char grade = 'A';
    cout<<"Grade: "<<grade<<endl;
    return 0;
}