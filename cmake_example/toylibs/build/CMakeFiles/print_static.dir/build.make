# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.21

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CMake.app/Contents/bin/cmake

# The command to remove a file.
RM = /Applications/CMake.app/Contents/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/zeyuanz/Downloads/toys/toylibs

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/zeyuanz/Downloads/toys/toylibs/build

# Include any dependencies generated for this target.
include CMakeFiles/print_static.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/print_static.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/print_static.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/print_static.dir/flags.make

CMakeFiles/print_static.dir/src/print.cpp.o: CMakeFiles/print_static.dir/flags.make
CMakeFiles/print_static.dir/src/print.cpp.o: ../src/print.cpp
CMakeFiles/print_static.dir/src/print.cpp.o: CMakeFiles/print_static.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/zeyuanz/Downloads/toys/toylibs/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/print_static.dir/src/print.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/print_static.dir/src/print.cpp.o -MF CMakeFiles/print_static.dir/src/print.cpp.o.d -o CMakeFiles/print_static.dir/src/print.cpp.o -c /Users/zeyuanz/Downloads/toys/toylibs/src/print.cpp

CMakeFiles/print_static.dir/src/print.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/print_static.dir/src/print.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/zeyuanz/Downloads/toys/toylibs/src/print.cpp > CMakeFiles/print_static.dir/src/print.cpp.i

CMakeFiles/print_static.dir/src/print.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/print_static.dir/src/print.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/zeyuanz/Downloads/toys/toylibs/src/print.cpp -o CMakeFiles/print_static.dir/src/print.cpp.s

CMakeFiles/print_static.dir/src/print_large.cpp.o: CMakeFiles/print_static.dir/flags.make
CMakeFiles/print_static.dir/src/print_large.cpp.o: ../src/print_large.cpp
CMakeFiles/print_static.dir/src/print_large.cpp.o: CMakeFiles/print_static.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/zeyuanz/Downloads/toys/toylibs/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/print_static.dir/src/print_large.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/print_static.dir/src/print_large.cpp.o -MF CMakeFiles/print_static.dir/src/print_large.cpp.o.d -o CMakeFiles/print_static.dir/src/print_large.cpp.o -c /Users/zeyuanz/Downloads/toys/toylibs/src/print_large.cpp

CMakeFiles/print_static.dir/src/print_large.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/print_static.dir/src/print_large.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/zeyuanz/Downloads/toys/toylibs/src/print_large.cpp > CMakeFiles/print_static.dir/src/print_large.cpp.i

CMakeFiles/print_static.dir/src/print_large.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/print_static.dir/src/print_large.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/zeyuanz/Downloads/toys/toylibs/src/print_large.cpp -o CMakeFiles/print_static.dir/src/print_large.cpp.s

# Object files for target print_static
print_static_OBJECTS = \
"CMakeFiles/print_static.dir/src/print.cpp.o" \
"CMakeFiles/print_static.dir/src/print_large.cpp.o"

# External object files for target print_static
print_static_EXTERNAL_OBJECTS =

../lib/libprint.a: CMakeFiles/print_static.dir/src/print.cpp.o
../lib/libprint.a: CMakeFiles/print_static.dir/src/print_large.cpp.o
../lib/libprint.a: CMakeFiles/print_static.dir/build.make
../lib/libprint.a: CMakeFiles/print_static.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/zeyuanz/Downloads/toys/toylibs/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX static library ../lib/libprint.a"
	$(CMAKE_COMMAND) -P CMakeFiles/print_static.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/print_static.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/print_static.dir/build: ../lib/libprint.a
.PHONY : CMakeFiles/print_static.dir/build

CMakeFiles/print_static.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/print_static.dir/cmake_clean.cmake
.PHONY : CMakeFiles/print_static.dir/clean

CMakeFiles/print_static.dir/depend:
	cd /Users/zeyuanz/Downloads/toys/toylibs/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/zeyuanz/Downloads/toys/toylibs /Users/zeyuanz/Downloads/toys/toylibs /Users/zeyuanz/Downloads/toys/toylibs/build /Users/zeyuanz/Downloads/toys/toylibs/build /Users/zeyuanz/Downloads/toys/toylibs/build/CMakeFiles/print_static.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/print_static.dir/depend

