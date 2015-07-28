#include <iostream>
#include<cstdlib>
#include<cstring>
using namespace std;

void reverse(char* arr, int len) {
  for(int i = 0; i<len/2; i++) {
    int j = len -1 - i;
    char temp = arr[j];
    arr[j] = arr[i];
    arr[i] = temp;
  }
}

char* func(const char *const arr, const int len) {
    
    if (len == 0){
      return nullptr;
    }
    else if (len == 1){
      return strdup(arr);
    }
    else{
      char * temp = new char[len];
      int x = len - 2 ;
      temp[0] = arr[len -1];
      int i = 1;
      int len_new = 1;
      while(x != 0){
        temp[i] = x%10 + '0';
        x = x/10;
        i++;
        len_new++;
      }
      len_new ++;
      temp[i] = arr[0];
      printf("%s\n", temp);
      reverse(temp, len_new);
      return temp;
    }
}

int main() {
  char inp[]  = "s";
  char *temp = func(inp , strlen(inp));
  printf("%s", temp );
  if(inp != nullptr){
    free(temp);
  }
  return 0;
}

