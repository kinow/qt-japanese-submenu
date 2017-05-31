cmake_minimum_required (VERSION 2.8.12)
project (kritaqtbug)

find_package(Qt5 5.6.0
        COMPONENTS
        Quick
        Core
        Gui
        Widgets
        Concurrent
)

# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)
# Instruct CMake to run moc automatically when needed.
set(CMAKE_AUTOMOC ON)

# Tell CMake to create the kritaqtbug executable
add_executable(kritaqtbug main)

# Use the Widgets module from Qt 5.
target_link_libraries(kritaqtbug Qt5::Widgets)
