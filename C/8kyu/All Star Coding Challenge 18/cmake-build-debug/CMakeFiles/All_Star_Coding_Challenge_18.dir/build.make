# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.17

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

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2019.3.3\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2019.3.3\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\8kyu\All Star Coding Challenge 18"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\8kyu\All Star Coding Challenge 18\cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/All_Star_Coding_Challenge_18.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/All_Star_Coding_Challenge_18.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/All_Star_Coding_Challenge_18.dir/flags.make

CMakeFiles/All_Star_Coding_Challenge_18.dir/main.c.obj: CMakeFiles/All_Star_Coding_Challenge_18.dir/flags.make
CMakeFiles/All_Star_Coding_Challenge_18.dir/main.c.obj: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\8kyu\All Star Coding Challenge 18\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/All_Star_Coding_Challenge_18.dir/main.c.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\All_Star_Coding_Challenge_18.dir\main.c.obj   -c "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\8kyu\All Star Coding Challenge 18\main.c"

CMakeFiles/All_Star_Coding_Challenge_18.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/All_Star_Coding_Challenge_18.dir/main.c.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\8kyu\All Star Coding Challenge 18\main.c" > CMakeFiles\All_Star_Coding_Challenge_18.dir\main.c.i

CMakeFiles/All_Star_Coding_Challenge_18.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/All_Star_Coding_Challenge_18.dir/main.c.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\8kyu\All Star Coding Challenge 18\main.c" -o CMakeFiles\All_Star_Coding_Challenge_18.dir\main.c.s

# Object files for target All_Star_Coding_Challenge_18
All_Star_Coding_Challenge_18_OBJECTS = \
"CMakeFiles/All_Star_Coding_Challenge_18.dir/main.c.obj"

# External object files for target All_Star_Coding_Challenge_18
All_Star_Coding_Challenge_18_EXTERNAL_OBJECTS =

All_Star_Coding_Challenge_18.exe: CMakeFiles/All_Star_Coding_Challenge_18.dir/main.c.obj
All_Star_Coding_Challenge_18.exe: CMakeFiles/All_Star_Coding_Challenge_18.dir/build.make
All_Star_Coding_Challenge_18.exe: CMakeFiles/All_Star_Coding_Challenge_18.dir/linklibs.rsp
All_Star_Coding_Challenge_18.exe: CMakeFiles/All_Star_Coding_Challenge_18.dir/objects1.rsp
All_Star_Coding_Challenge_18.exe: CMakeFiles/All_Star_Coding_Challenge_18.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\8kyu\All Star Coding Challenge 18\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable All_Star_Coding_Challenge_18.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\All_Star_Coding_Challenge_18.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/All_Star_Coding_Challenge_18.dir/build: All_Star_Coding_Challenge_18.exe

.PHONY : CMakeFiles/All_Star_Coding_Challenge_18.dir/build

CMakeFiles/All_Star_Coding_Challenge_18.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\All_Star_Coding_Challenge_18.dir\cmake_clean.cmake
.PHONY : CMakeFiles/All_Star_Coding_Challenge_18.dir/clean

CMakeFiles/All_Star_Coding_Challenge_18.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\8kyu\All Star Coding Challenge 18" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\8kyu\All Star Coding Challenge 18" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\8kyu\All Star Coding Challenge 18\cmake-build-debug" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\8kyu\All Star Coding Challenge 18\cmake-build-debug" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\8kyu\All Star Coding Challenge 18\cmake-build-debug\CMakeFiles\All_Star_Coding_Challenge_18.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/All_Star_Coding_Challenge_18.dir/depend
