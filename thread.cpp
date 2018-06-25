#include<iostream>
#include<thread>
using namespace std;

void thread_func(int i){
cout<<"\nInside thread :"<<i<<endl;
}

int main(){
	thread t(thread_func,5);
return 0;
}
