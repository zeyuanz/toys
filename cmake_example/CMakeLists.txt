cmake_minimum_required(VERSION 3.10)

project(tutorial VERSION 1.0)

# file(GLOB sources src/*.cpp)

# add_executable(test main.cpp ${sources})

set(SRC_LIST ${PROJECT_SOURCE_DIR}/main.cpp)

include_directories(${PROJECT_SOURCE_DIR}/toylibs/include)
find_library(PRINTLIB print HINTS ${PROJECT_SOURCE_DIR}/toylibs/lib)

add_executable(main ${SRC_LIST})
target_link_libraries(main ${PRINTLIB})
