cmake_minimum_required(VERSION 3.10)

project(tutorial VERSION 1.0)

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
file(GLOB sources src/*.cpp)

add_executable(tax main.cpp ${sources})
