#include <cstdlib> 
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int fib(); 

	private:
		int age;
		int fib_p(int);
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}

int Person::fib(){
	return fib_p(age);
	}	

int  Person::fib_p(int n){
	 if n <= 1:
		return n;
	 else:
		return(fib_py(n-1) + fib_py(n-2));
	}

void Person::set(int n){
	age = n;
	}

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}