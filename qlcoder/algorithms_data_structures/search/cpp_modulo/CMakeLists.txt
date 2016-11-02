cmake_minimum_required(VERSION 3.6)
project(cpp_modulo)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp state_space_search.h state_space_search.cpp)
add_executable(cpp_modulo ${SOURCE_FILES})