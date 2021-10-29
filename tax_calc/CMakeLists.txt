cmake_minimum_required(VERSION 3.10)

project(tutorial VERSION 1.0)

file(GLOB sources src/*.cpp)

add_executable(main main.cpp ${sources})
