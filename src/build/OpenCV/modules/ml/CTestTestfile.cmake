# CMake generated Testfile for 
# Source directory: /home/orin/test_ws/src/opencv/modules/ml
# Build directory: /home/orin/test_ws/src/build/OpenCV/modules/ml
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_ml "/home/orin/test_ws/src/build/OpenCV/bin/opencv_test_ml" "--gtest_output=xml:opencv_test_ml.xml")
set_tests_properties(opencv_test_ml PROPERTIES  LABELS "Main;opencv_ml;Accuracy" WORKING_DIRECTORY "/home/orin/test_ws/src/build/OpenCV/test-reports/accuracy" _BACKTRACE_TRIPLES "/home/orin/test_ws/src/opencv/cmake/OpenCVUtils.cmake;1799;add_test;/home/orin/test_ws/src/opencv/cmake/OpenCVModule.cmake;1365;ocv_add_test_from_target;/home/orin/test_ws/src/opencv/cmake/OpenCVModule.cmake;1123;ocv_add_accuracy_tests;/home/orin/test_ws/src/opencv/modules/ml/CMakeLists.txt;2;ocv_define_module;/home/orin/test_ws/src/opencv/modules/ml/CMakeLists.txt;0;")
