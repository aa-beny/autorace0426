# Install script for directory: /home/orin/test_ws/src/opencv

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/orin/test_ws/src/install/OpenCV")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "licenses" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/licenses/opencv4" TYPE FILE RENAME "flatbuffers-LICENSE.txt" FILES "/home/orin/test_ws/src/opencv/3rdparty/flatbuffers/LICENSE.txt")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "licenses" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/licenses/opencv4" TYPE FILE RENAME "opencl-headers-LICENSE.txt" FILES "/home/orin/test_ws/src/opencv/3rdparty/include/opencl/LICENSE.txt")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "licenses" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/licenses/opencv4" TYPE FILE RENAME "ade-LICENSE" FILES "/home/orin/test_ws/src/build/OpenCV/3rdparty/ade/ade-0.1.2e/LICENSE")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "dev" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv4/opencv2" TYPE FILE FILES "/home/orin/test_ws/src/build/OpenCV/cvconfig.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "dev" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv4/opencv2" TYPE FILE FILES "/home/orin/test_ws/src/build/OpenCV/opencv2/opencv_modules.hpp")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "dev" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/opencv4/OpenCVModules.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/opencv4/OpenCVModules.cmake"
         "/home/orin/test_ws/src/build/OpenCV/CMakeFiles/Export/51ea738ee2ea68756d9122094dacc2a4/OpenCVModules.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/opencv4/OpenCVModules-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/opencv4/OpenCVModules.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/opencv4" TYPE FILE FILES "/home/orin/test_ws/src/build/OpenCV/CMakeFiles/Export/51ea738ee2ea68756d9122094dacc2a4/OpenCVModules.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/opencv4" TYPE FILE FILES "/home/orin/test_ws/src/build/OpenCV/CMakeFiles/Export/51ea738ee2ea68756d9122094dacc2a4/OpenCVModules-release.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "dev" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/opencv4" TYPE FILE FILES
    "/home/orin/test_ws/src/build/OpenCV/unix-install/OpenCVConfig-version.cmake"
    "/home/orin/test_ws/src/build/OpenCV/unix-install/OpenCVConfig.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "scripts" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE FILE PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE FILES "/home/orin/test_ws/src/build/OpenCV/CMakeFiles/install/setup_vars_opencv4.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "dev" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opencv4" TYPE FILE FILES
    "/home/orin/test_ws/src/opencv/platforms/scripts/valgrind.supp"
    "/home/orin/test_ws/src/opencv/platforms/scripts/valgrind_3rdparty.supp"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/orin/test_ws/src/build/OpenCV/3rdparty/openexr/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/3rdparty/protobuf/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/3rdparty/carotene/hal/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/3rdparty/ittnotify/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/include/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/calib3d/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/core/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/dnn/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/features2d/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/flann/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/gapi/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/highgui/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/imgcodecs/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/imgproc/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/java/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/js/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/ml/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/objc/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/objdetect/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/photo/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/python/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/stitching/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/ts/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/video/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/videoio/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/.firstpass/world/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/core/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/flann/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/imgproc/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/ml/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/photo/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/python_tests/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/dnn/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/features2d/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/imgcodecs/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/videoio/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/calib3d/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/highgui/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/objdetect/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/stitching/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/ts/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/video/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/gapi/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/java_bindings_generator/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/js_bindings_generator/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/objc_bindings_generator/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/python_bindings_generator/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/modules/python3/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/doc/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/data/cmake_install.cmake")
  include("/home/orin/test_ws/src/build/OpenCV/apps/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/orin/test_ws/src/build/OpenCV/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
