#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int T;
    double A,B,C;
    cin>>T; 
    
    for(int i =0; i<T;i++)
    {
        
    cin>>A>>B>>C;
    cout<<left<<nouppercase<<hex<<showbase<<(long long)A<<endl;
    cout<<setfill('_')<<setw(15)<<right<<showpos<<fixed<<setprecision(2)<<B<<endl;
    cout<<setprecision(9)<<noshowpos<<scientific<<uppercase<<C<<endl;
    }
    return 0;
}
