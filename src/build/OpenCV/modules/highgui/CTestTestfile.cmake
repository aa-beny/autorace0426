# CMake generated Testfile for 
# Source directory: /home/orin/test_ws/src/opencv/modules/highgui
# Build directory: /home/orin/test_ws/src/build/OpenCV/modules/highgui
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_highgui "/home/orin/test_ws/src/build/OpenCV/bin/opencv_test_highgui" "--gtest_output=xml:opencv_test_highgui.xml")
set_tests_properties(opencv_test_highgui PROPERTIES  LABELS "Main;opencv_highgui;Accuracy" WORKING_DIRECTORY "/home/orin/test_ws/src/build/OpenCV/test-reports/accuracy" _BACKTRACE_TRIPLES "/home/orin/test_ws/src/opencv/cmake/OpenCVUtils.cmake;1799;add_test;/home/orin/test_ws/src/opencv/cmake/OpenCVModule.cmake;1365;ocv_add_test_from_target;/home/orin/test_ws/src/opencv/modules/highgui/CMakeLists.txt;311;ocv_add_accuracy_tests;/home/orin/test_ws/src/opencv/modules/highgui/CMakeLists.txt;0;")
