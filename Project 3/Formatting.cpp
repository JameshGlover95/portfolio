#include "Formatting.h"
#include <string>
#include <iostream>
using namespace std;

string Formatting::nCharString(int n, char c) {
	temp = "";
	for (int i = 0; i <= n; i++) {
		temp = temp + c;
	}
	// return the n character string
	return temp;
}
void Formatting::PrintMenu()
{
	cout << nCharString(70, '*') << endl;
	cout << "	1. list all items purchased with quantity." << endl;
	cout << "	2. Show the number of times a specific item was purchased." << endl;
	cout << "	3. Histograph of items purchased." << endl;
	cout << "	4. Exit Program." << endl;
	cout << nCharString(70, '*') << endl;
}
;