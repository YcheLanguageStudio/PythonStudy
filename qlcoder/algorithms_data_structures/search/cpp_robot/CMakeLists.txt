cmake_minimum_required(VERSION 3.5)
project(cpp_robot)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -g -O3")

set(SOURCE_FILES main.cpp state_space_search.cpp state_space_search.h)
add_executable(cpp_robot ${SOURCE_FILES})