#include <iostream>
#include <vector>
#include <algorithm>
#include<functional>

template<typename T>
void show(std::string s,std::vector<T> vec){
    std::cout << s << std::endl;
    std::for_each(vec.begin(), vec.end(), [](int& n){std::cout << n << " ";});
    std::cout<<std::endl;
    
}

int main()
{
    ///////part A //////////
    std::vector<int> vec1(100);
    std::vector<int> vec2(10);
    int i{1};
    std::for_each(vec1.begin(), vec1.end(), [&i](int& n){n = i++;});
    show("vec1 : ", vec1);
    i = 1;
    std::for_each(vec2.begin(), vec2.end(), [&i](int& n){n = i++;});
    show("vec2 : ", vec1);
    ///////part B //////////
    std::copy(vec1.begin(), vec1.end(), std::back_inserter(vec2));
    show("vec2 + vec1 : ", vec1);
    ///////part C //////////
    std::vector<int> odd_vec;
    std::for_each(vec1.begin(), vec1.end(), [&odd_vec](int& n){if(n %2 == 1){odd_vec.push_back(n);};});
    show("odd vec : ",odd_vec);
    ///////part D //////////
    i = vec1.size();
    std::vector<int> reverse_vec(i);
    for_each(vec1.begin(), vec1.end(), [&reverse_vec, &i](int& n){reverse_vec.at(--i) = n;});
    show("reverse vec : ",reverse_vec);
    
    return 0;
}