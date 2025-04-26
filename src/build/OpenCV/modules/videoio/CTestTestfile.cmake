# CMake generated Testfile for 
# Source directory: /home/orin/test_ws/src/opencv/modules/videoio
# Build directory: /home/orin/test_ws/src/build/OpenCV/modules/videoio
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_videoio "/home/orin/test_ws/src/build/OpenCV/bin/opencv_test_videoio" "--gtest_output=xml:opencv_test_videoio.xml")
set_tests_properties(opencv_test_videoio PROPERTIES  LABELS "Main;opencv_videoio;Accuracy" WORKING_DIRECTORY "/home/orin/test_ws/src/build/OpenCV/test-reports/accuracy" _BACKTRACE_TRIPLES "/home/orin/test_ws/src/opencv/cmake/OpenCVUtils.cmake;1799;add_test;/home/orin/test_ws/src/opencv/cmake/OpenCVModule.cmake;1365;ocv_add_test_from_target;/home/orin/test_ws/src/opencv/modules/videoio/CMakeLists.txt;281;ocv_add_accuracy_tests;/home/orin/test_ws/src/opencv/modules/videoio/CMakeLists.txt;0;")
add_test(opencv_perf_videoio "/home/orin/test_ws/src/build/OpenCV/bin/opencv_perf_videoio" "--gtest_output=xml:opencv_perf_videoio.xml")
set_tests_properties(opencv_perf_videoio PROPERTIES  LABELS "Main;opencv_videoio;Performance" WORKING_DIRECTORY "/home/orin/test_ws/src/build/OpenCV/test-reports/performance" _BACKTRACE_TRIPLES "/home/orin/test_ws/src/opencv/cmake/OpenCVUtils.cmake;1799;add_test;/home/orin/test_ws/src/opencv/cmake/OpenCVModule.cmake;1264;ocv_add_test_from_target;/home/orin/test_ws/src/opencv/modules/videoio/CMakeLists.txt;282;ocv_add_perf_tests;/home/orin/test_ws/src/opencv/modules/videoio/CMakeLists.txt;0;")
add_test(opencv_sanity_videoio "/home/orin/test_ws/src/build/OpenCV/bin/opencv_perf_videoio" "--gtest_output=xml:opencv_perf_videoio.xml" "--perf_min_samples=1" "--perf_force_samples=1" "--perf_verify_sanity")
set_tests_properties(opencv_sanity_videoio PROPERTIES  LABELS "Main;opencv_videoio;Sanity" WORKING_DIRECTORY "/home/orin/test_ws/src/build/OpenCV/test-reports/sanity" _BACKTRACE_TRIPLES "/home/orin/test_ws/src/opencv/cmake/OpenCVUtils.cmake;1799;add_test;/home/orin/test_ws/src/opencv/cmake/OpenCVModule.cmake;1265;ocv_add_test_from_target;/home/orin/test_ws/src/opencv/modules/videoio/CMakeLists.txt;282;ocv_add_perf_tests;/home/orin/test_ws/src/opencv/modules/videoio/CMakeLists.txt;0;")
