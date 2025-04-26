// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from detect_interfaces:msg/BoundingBox.idl
// generated code does not contain a copyright notice

#ifndef DETECT_INTERFACES__MSG__DETAIL__BOUNDING_BOX__STRUCT_H_
#define DETECT_INTERFACES__MSG__DETAIL__BOUNDING_BOX__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/BoundingBox in the package detect_interfaces.
typedef struct detect_interfaces__msg__BoundingBox
{
  int32_t xmin;
  int32_t ymin;
  int32_t xmax;
  int32_t ymax;
} detect_interfaces__msg__BoundingBox;

// Struct for a sequence of detect_interfaces__msg__BoundingBox.
typedef struct detect_interfaces__msg__BoundingBox__Sequence
{
  detect_interfaces__msg__BoundingBox * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} detect_interfaces__msg__BoundingBox__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DETECT_INTERFACES__MSG__DETAIL__BOUNDING_BOX__STRUCT_H_
