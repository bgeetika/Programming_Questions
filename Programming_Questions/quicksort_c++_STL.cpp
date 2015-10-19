#include <iostream>
#include <vector>
#include <string>
#include <iterator>
#include <cstdlib>
#include <map>


using namespace std;

int parti(vector<int> *input, int start, int end) {
    int pivot = rand()%(end-start + 1) + start;
    swap(input->at(pivot),input->at(end));
    int i = start - 1;
  while( start <= end ) { 
      if ((*input)[start] < (*input)[pivot]){
            i++;
            swap(input->at(start) , input->at(i));
      }
      start++;
    } 
    i++;
    swap(input->at(end) , input->at(i));   
    return i;
}

void quicksort(vector<int> *input, int start, int end) {
   if (start <= end){
     int partition = parti(input, start, end);
     quicksort(input, partition + 1, end);
     quicksort(input, start, partition - 1);
   }
}


char uniquechar(const vector<char> *input) {
  map<char, int> CountMap;
   map<char, int>::iterator res;
  int i = 0;
  for (auto x : *input) {
     res = CountMap.find(x);
     if (res!=CountMap.end()) {
       CountMap.erase(res);
     }
     else {
       CountMap.insert(std::pair<char, int>(x,i));
     }
  i++;
}

  // prefer using ->
  int min = input->size();
  for (res = CountMap.begin(); res!=CountMap.end(); ++res){
    if (res->second < min) {
      min = res->second;
    }
    
  }
  return (*input)[min];
}


int main() {
  vector<char> input ;
  //cout << sizeof(input);
  
  
  input.push_back('a');
  input.push_back('a');
  input.push_back('b');
  input.push_back('d');
  input.push_back('c');
  input.push_back('b');
  
 
  //quicksort(&input, 0 , input.size() - 1);
  char x;
  x = uniquechar(&input);
  cout<<x;
  
  
  return 0;
}

