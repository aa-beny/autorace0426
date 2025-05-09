// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from detect_interfaces:msg/BoundingBox.idl
// generated code does not contain a copyright notice

#ifndef DETECT_INTERFACES__MSG__DETAIL__BOUNDING_BOX__BUILDER_HPP_
#define DETECT_INTERFACES__MSG__DETAIL__BOUNDING_BOX__BUILDER_HPP_

#include "detect_interfaces/msg/detail/bounding_box__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace detect_interfaces
{

namespace msg
{

namespace builder
{

class Init_BoundingBox_ymax
{
public:
  explicit Init_BoundingBox_ymax(::detect_interfaces::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  ::detect_interfaces::msg::BoundingBox ymax(::detect_interfaces::msg::BoundingBox::_ymax_type arg)
  {
    msg_.ymax = std::move(arg);
    return std::move(msg_);
  }

private:
  ::detect_interfaces::msg::BoundingBox msg_;
};

class Init_BoundingBox_xmax
{
public:
  explicit Init_BoundingBox_xmax(::detect_interfaces::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  Init_BoundingBox_ymax xmax(::detect_interfaces::msg::BoundingBox::_xmax_type arg)
  {
    msg_.xmax = std::move(arg);
    return Init_BoundingBox_ymax(msg_);
  }

private:
  ::detect_interfaces::msg::BoundingBox msg_;
};

class Init_BoundingBox_ymin
{
public:
  explicit Init_BoundingBox_ymin(::detect_interfaces::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  Init_BoundingBox_xmax ymin(::detect_interfaces::msg::BoundingBox::_ymin_type arg)
  {
    msg_.ymin = std::move(arg);
    return Init_BoundingBox_xmax(msg_);
  }

private:
  ::detect_interfaces::msg::BoundingBox msg_;
};

class Init_BoundingBox_xmin
{
public:
  Init_BoundingBox_xmin()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BoundingBox_ymin xmin(::detect_interfaces::msg::BoundingBox::_xmin_type arg)
  {
    msg_.xmin = std::move(arg);
    return Init_BoundingBox_ymin(msg_);
  }

private:
  ::detect_interfaces::msg::BoundingBox msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::detect_interfaces::msg::BoundingBox>()
{
  return detect_interfaces::msg::builder::Init_BoundingBox_xmin();
}

}  // namespace detect_interfaces

#endif  // DETECT_INTERFACES__MSG__DETAIL__BOUNDING_BOX__BUILDER_HPP_
