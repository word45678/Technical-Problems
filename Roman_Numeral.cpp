#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int romanNumeral(string numb){
    int spot = 0;
    int sum = 0;
    int next = 0;
    unordered_map<char,int> symbols{
        {'I',1},
        {'V',5},
        {'X',10},
        {'L',50},
        {'C',100},
        {'D',500},
        {'M',1000}
    };
    while(spot<numb.length()-1){
        next = symbols[numb.at(spot)];
        if(symbols[numb.at(spot)]<symbols[numb.at(spot+1)]){
            next = next * -1;
        }
        sum += next;
        spot++;
    }
    sum += symbols[numb.at(numb.length()-1)];
    return sum;
}

int main(){
    string roman;
    cout<<"Please enter your Roman numeral: ";
    getline(cin, roman);
    cout<<"Your Roman numeral: "<<roman<<" yielded "<< romanNumeral(roman)<< " in Arabic numerals\n";
    return 0;
}