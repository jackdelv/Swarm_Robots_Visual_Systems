# cmake needs this line
cmake_minimum_required(VERSION 3.1)
# Define project name
project(camera_example_project)

# Find OpenCV, you may need to set OpenCV_DIR variable
# to the absolute path to the directory containing OpenCVConfig.cmake file
# via the command line or GUI
find_package(OpenCV REQUIRED)
# If the package has been found, several variables will
# be set, you can find the full list with descriptions
# in the OpenCVConfig.cmake file.
# Print some message showing some of them
message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

include_directories(.)
# Declare the executable target built from your sources
#add_executable(square_detect square_detect.cpp)
add_executable(squares_test squares_test.cpp)

find_library(WIRINGPI_LIBRARIES NAMES wiringPi)
# Link your application with OpenCV libraries
target_link_libraries(squares_test PRIVATE ${OpenCV_LIBS})
target_link_libraries(squares_test PRIVATE ${WIRINGPI_LIBRARIES})
