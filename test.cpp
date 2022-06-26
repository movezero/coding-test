#include <iostream>
using namespace std;

int find(int* array,int num)
{
   int i, j;
   for (i = 0; i < 10; i++)
   {
      if (array[i] == array[num])
         j = 0;
      else
         j = 1;
   }
   return j;
};

void getArray(int* array,int& count)
{
   int num;
   int j;
   cin >> num;
   array[count] = num;
   j = find(array,num);
   if (j = 0)
      array[count] = 0;
   else
      array[count] = num;
   count++;
};

int main()
{
   int count = 1;
   int i;
   int array[20] = { 0 };
   while (1)
   {
      getArray(array, count);
      for (i = 0; i < count; i++)
         cout << array[i];
      cout << endl;
   }
   return 0;
}