#include <stdio.h>
#include <windows.h>

int main(){
	HMODULE lib = LoadLibrary("HowDoesThisWork.dll");
	if(lib){
		printf("Success");
		func();
	}
	else{
		printf("fail");
	}
	return 0;
}
