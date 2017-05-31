#!/bin/bash

cmake -G "Eclipse CDT4 - Unix Makefiles" ../cpp -DCMAKE_CXX_FLAGS="-O0 -g" -DCFLAGS="-O0 -g" -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS_DEBUG="-O0 -g"

make -j8

exit 0
