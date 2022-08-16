#include "GettersSetters.h"
#include <string>
#include <iostream>
using namespace std;

	unsigned int GettersSetters::getMenuChoice(unsigned int maxChoice)
	{
		bool valid = false;
		while (valid == false) {
			int input;
			cin >> input;
			if (input >= 1 and input <= maxChoice) {
				valid = true;
				return input;
			}
		}
	}
