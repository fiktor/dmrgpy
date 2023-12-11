// SPDX-License-Identifier: GPL-3.0-or-later
#ifndef __MPSCPP2_CHECK_TASK_H
#define __MPSCPP2_CHECK_TASK_H
// check if this task should be performed

static auto check_task = [](auto name) {
  // bool check_task(auto name) {
  auto input = InputGroup("tasks.in", "tasks");
  auto dotask = input.getYesNo(name, false);
  return dotask;
};

// functions to get data from the input file

static auto get_int_value = [](auto name) {
  auto input = InputGroup("tasks.in", "tasks");
  auto N = input.getInt(name, 1);
  return N;
};

static auto get_float_value = [](auto name) {
  auto input = InputGroup("tasks.in", "tasks");
  auto N = input.getReal(name, 0.0);
  return N;
};

static auto get_str = [](auto name) {
  auto input = InputGroup("tasks.in", "tasks");
  return input.getString(name, "");
};

static auto get_bool = [](auto name) {
  auto input = InputGroup("tasks.in", "tasks");
  auto dotask = input.getYesNo(name, false);
  return dotask;
};
#endif // __MPSCPP2_CHECK_TASK_H
