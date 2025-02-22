load("@rules_python//python:defs.bzl", "py_library", "py_test")
load("@bazel_skylib//rules:common.bzl", "sh_test")


py_library(
    name = "math_utils",
    srcs = ["src/math_utils.py"],
    visibility = ["//visibility:public"],
)

py_library(
    name = "string_utils",
    srcs = ["src/string_utils.py"],
    visibility = ["//visibility:public"],
)


py_test(
    name = "test_math_utils",
    srcs = ["tests/test_math_utils.py"],
    deps = [":math_utils"],
)

py_test(
    name = "test_string_utils",
    srcs = ["tests/test_string_utils.py"],
    deps = [":string_utils"],
)


sh_test(
    name = "lint",
    srcs = ["scripts/lint.sh"],
)


sh_test(
    name = "format",
    srcs = ["scripts/format.sh"],
)