// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from detect_interfaces:msg/BoundingBox.idl
// generated code does not contain a copyright notice

#ifndef DETECT_INTERFACES__MSG__DETAIL__BOUNDING_BOX__TRAITS_HPP_
#define DETECT_INTERFACES__MSG__DETAIL__BOUNDING_BOX__TRAITS_HPP_

#include "detect_interfaces/msg/detail/bounding_box__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<detect_interfaces::msg::BoundingBox>()
{
  return "detect_interfaces::msg::BoundingBox";
}

template<>
inline const char * name<detect_interfaces::msg::BoundingBox>()
{
  return "detect_interfaces/msg/BoundingBox";
}

template<>
struct has_fixed_size<detect_interfaces::msg::BoundingBox>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<detect_interfaces::msg::BoundingBox>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<detect_interfaces::msg::BoundingBox>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DETECT_INTERFACES__MSG__DETAIL__BOUNDING_BOX__TRAITS_HPP_
