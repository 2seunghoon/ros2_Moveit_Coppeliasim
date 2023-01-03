# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_dyros_urdf_tf_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED dyros_urdf_tf_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(dyros_urdf_tf_FOUND FALSE)
  elseif(NOT dyros_urdf_tf_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(dyros_urdf_tf_FOUND FALSE)
  endif()
  return()
endif()
set(_dyros_urdf_tf_CONFIG_INCLUDED TRUE)

# output package information
if(NOT dyros_urdf_tf_FIND_QUIETLY)
  message(STATUS "Found dyros_urdf_tf: 0.0.0 (${dyros_urdf_tf_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'dyros_urdf_tf' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${dyros_urdf_tf_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(dyros_urdf_tf_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${dyros_urdf_tf_DIR}/${_extra}")
endforeach()
