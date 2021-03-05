---
title: "C++ 的 new、delete 与 C 的 malloc、free 的区别"
date: 2014-11-24T19:12:27+08:00
draft: false
tags: [c++,c]
categories: [c++,c]
---
小程序以验证C/C++内存管理的差异（写的不是很严谨，仅为主题，分别在redhat 5.6 x86_64 + gcc-4.9.2，windows 7 x64 + gcc-4.9.2 编译运行通过）：
```c++
#include <iostream>
#include <typeinfo>
#include <stdlib.h>
#include <stdio.h>
void t_cpu()
{
#define print_type(t) std::cout << "Size of " << #t <<  ": " << sizeof(t) << std::endl
    print_type(char);
    print_type(unsigned char);
    print_type(short);
    print_type(unsigned short);
    print_type(int);
    print_type(unsigned int);
    print_type(size_t);
    print_type(long);
    print_type(unsigned long);
    print_type(long long);
    print_type(unsigned long long);
    print_type(float);
    print_type(double);
    print_type(long double);
    print_type(void*);
 
}
 
class __T {
public:
    int _1;
    int _2;
 
    __T(){
        _1 = 1;
        _2 = 2;
    }
    ~__T(){
        printf("~");
    }
 
    void init()
    {
        _1 = 7;
        _2 = 8;
    }
 
    void test()
    {
        _1 += _2;
    }
};
 
void t_new(size_t sl)
{
    __T *pchar = new __T[sl];
    size_t  *psize  = (size_t*)(((char*)pchar)-sizeof(size_t));
    printf("\nTest new and delete \nsize: %ld pchar: %p psize: %p *psize: %ld \n", sl, pchar, psize, *psize);
    delete []pchar;
    printf("\n");
}
 
void t_malloc(size_t sl)
{
    printf("\nTest malloc and free \nsize of class __T: %ld  \n", sizeof(class __T));
    __T *pchar = (__T *)malloc(sl * sizeof(class __T));
    size_t  *psize  = (size_t*)(((char*)pchar)-sizeof(size_t));
    printf("size: %ld pchar: %p psize: %p *psize: %ld \n", sl, pchar, psize, *psize);
    free(pchar);
}
 
void t_new_free(size_t sl)
{
    __T *pchar = new __T[sl];
    size_t  *psize  = (size_t*)(((char*)pchar)-sizeof(size_t));
    printf("\nTest new and free \nsize: %ld pchar: %p psize: %p *psize: %ld \n", sl, pchar, psize, *psize);
    //delete []pchar;
    for (__T *t = pchar; t < pchar + sl; ++t) {
        t->~__T();
    }
 
    free(psize);
    printf("\n");
}
 
void t_malloc_delete(size_t sl)
{
    printf("\nTest malloc and delete \nsize of class __T: %ld  \n", sizeof(class __T));
    size_t *psize = (size_t *)malloc(sl * sizeof(class __T) + sizeof(size_t));
    __T  *pchar  = (__T*)(((char*)psize)+sizeof(size_t));
    *psize = sl;
    //for (__T *t = pchar; t < pchar + sl; ++t) {
    //    t->init();
    //}
    printf("size: %ld pchar: %p psize: %p *psize: %ld \n", sl, pchar, psize, *psize);
    delete [] pchar;
    printf("\n");
}
 
int main()
{
    t_cpu();
    t_new(48);
    t_malloc(32);
    t_new_free(16);
    t_malloc_delete(8);
    return 0;
}
```
输出（redhat）：
```c++
Size of char: 1
Size of unsigned char: 1
Size of short: 2
Size of unsigned short: 2
Size of int: 4
Size of unsigned int: 4
Size of size_t: 8
Size of long: 8
Size of unsigned long: 8
Size of long long: 8
Size of unsigned long long: 8
Size of float: 4
Size of double: 8
Size of long double: 16
Size of void*: 8

Test new and delete 
size: 48 pchar: 0x2442018 psize: 0x2442010 *psize: 48 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test malloc and free 
size of class __T: 8  
size: 32 pchar: 0x2442010 psize: 0x2442008 *psize: 273 

Test new and free 
size: 16 pchar: 0x2442018 psize: 0x2442010 *psize: 16 
~~~~~~~~~~~~~~~~

Test malloc and delete 
size of class __T: 8  
size: 8 pchar: 0x2442018 psize: 0x2442010 *psize: 8 
~~~~~~~~
```
输出（Windows）：
```c++
Size of char: 1
Size of unsigned char: 1
Size of short: 2
Size of unsigned short: 2
Size of int: 4
Size of unsigned int: 4
Size of size_t: 4
Size of long: 4
Size of unsigned long: 4
Size of long long: 8
Size of unsigned long long: 8
Size of float: 4
Size of double: 8
Size of long double: 12
Size of void*: 4

Test new and delete
size: 48 pchar: 00991b54 psize: 00991b50 *psize: 48
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test malloc and free
size of class __T: 8
size: 32 pchar: 00991b50 psize: 00991b4c *psize: 134253675

Test new and free
size: 16 pchar: 00991b54 psize: 00991b50 *psize: 16
~~~~~~~~~~~~~~~~

Test malloc and delete
size of class __T: 8
size: 8 pchar: 00991b54 psize: 00991b50 *psize: 8
~~~~~~~~
```

