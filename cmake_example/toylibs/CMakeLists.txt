cmake_minimum_required(VERSION 3.10)

project(demo)

set(SRC_LISTS ${PROJECT_SOURCE_DIR}/src/print.cpp ${PROJECT_SOURCE_DIR}/src/print_large.cpp)

add_library(print_shared SHARED ${SRC_LISTS})
add_library(print_static STATIC ${SRC_LISTS})

set_target_properties(print_shared PROPERTIES OUTPUT_NAME "print")
set_target_properties(print_static PROPERTIES OUTPUT_NAME "print")
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)


