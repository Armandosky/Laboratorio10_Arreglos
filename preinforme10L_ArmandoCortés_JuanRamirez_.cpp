#include<iostream>
#include<conio.h>

using namespace std;

int main()
{
	int n[100][100], filas, columnas;
	
	cout << "Ingrese el n�mero de filas: ";
	cin>>filas;
	cout << "Ingrese el n�mero de columnas: ";
	cin>>columnas;
	
	for(int i=0; i < filas; i++)
	{
		for (int c=0;c<columnas;c++)
		{
			cout << "Ingrese un n�mero["<<i<<"]["<<c<<"]" ;
			cin >> n[i][c];
		}
	}
	
	for(int i=0; i < filas; i++)
	{
		for (int c=0; c<columnas;c++)
		{
			cout << n [i][c];
		}
	}
	
	
	
	printf("\n\n\n");system("PAUSE");
	return 0;
}
