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
CMAKE_SOURCE_DIR = "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Square Every Digit"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Square Every Digit\cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/Square_Every_Digit.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Square_Every_Digit.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Square_Every_Digit.dir/flags.make

CMakeFiles/Square_Every_Digit.dir/main.c.obj: CMakeFiles/Square_Every_Digit.dir/flags.make
CMakeFiles/Square_Every_Digit.dir/main.c.obj: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Square Every Digit\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/Square_Every_Digit.dir/main.c.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\Square_Every_Digit.dir\main.c.obj   -c "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Square Every Digit\main.c"

CMakeFiles/Square_Every_Digit.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/Square_Every_Digit.dir/main.c.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Square Every Digit\main.c" > CMakeFiles\Square_Every_Digit.dir\main.c.i

CMakeFiles/Square_Every_Digit.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/Square_Every_Digit.dir/main.c.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Square Every Digit\main.c" -o CMakeFiles\Square_Every_Digit.dir\main.c.s

# Object files for target Square_Every_Digit
Square_Every_Digit_OBJECTS = \
"CMakeFiles/Square_Every_Digit.dir/main.c.obj"

# External object files for target Square_Every_Digit
Square_Every_Digit_EXTERNAL_OBJECTS =

Square_Every_Digit.exe: CMakeFiles/Square_Every_Digit.dir/main.c.obj
Square_Every_Digit.exe: CMakeFiles/Square_Every_Digit.dir/build.make
Square_Every_Digit.exe: CMakeFiles/Square_Every_Digit.dir/linklibs.rsp
Square_Every_Digit.exe: CMakeFiles/Square_Every_Digit.dir/objects1.rsp
Square_Every_Digit.exe: CMakeFiles/Square_Every_Digit.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Square Every Digit\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable Square_Every_Digit.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\Square_Every_Digit.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Square_Every_Digit.dir/build: Square_Every_Digit.exe

.PHONY : CMakeFiles/Square_Every_Digit.dir/build

CMakeFiles/Square_Every_Digit.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Square_Every_Digit.dir\cmake_clean.cmake
.PHONY : CMakeFiles/Square_Every_Digit.dir/clean

CMakeFiles/Square_Every_Digit.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Square Every Digit" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Square Every Digit" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Square Every Digit\cmake-build-debug" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Square Every Digit\cmake-build-debug" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Square Every Digit\cmake-build-debug\CMakeFiles\Square_Every_Digit.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Square_Every_Digit.dir/depend
