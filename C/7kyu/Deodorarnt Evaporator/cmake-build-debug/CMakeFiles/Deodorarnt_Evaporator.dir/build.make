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
CMAKE_SOURCE_DIR = "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Deodorarnt Evaporator"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Deodorarnt Evaporator\cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/Deodorarnt_Evaporator.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Deodorarnt_Evaporator.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Deodorarnt_Evaporator.dir/flags.make

CMakeFiles/Deodorarnt_Evaporator.dir/main.c.obj: CMakeFiles/Deodorarnt_Evaporator.dir/flags.make
CMakeFiles/Deodorarnt_Evaporator.dir/main.c.obj: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Deodorarnt Evaporator\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/Deodorarnt_Evaporator.dir/main.c.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\Deodorarnt_Evaporator.dir\main.c.obj   -c "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Deodorarnt Evaporator\main.c"

CMakeFiles/Deodorarnt_Evaporator.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/Deodorarnt_Evaporator.dir/main.c.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Deodorarnt Evaporator\main.c" > CMakeFiles\Deodorarnt_Evaporator.dir\main.c.i

CMakeFiles/Deodorarnt_Evaporator.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/Deodorarnt_Evaporator.dir/main.c.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Deodorarnt Evaporator\main.c" -o CMakeFiles\Deodorarnt_Evaporator.dir\main.c.s

# Object files for target Deodorarnt_Evaporator
Deodorarnt_Evaporator_OBJECTS = \
"CMakeFiles/Deodorarnt_Evaporator.dir/main.c.obj"

# External object files for target Deodorarnt_Evaporator
Deodorarnt_Evaporator_EXTERNAL_OBJECTS =

Deodorarnt_Evaporator.exe: CMakeFiles/Deodorarnt_Evaporator.dir/main.c.obj
Deodorarnt_Evaporator.exe: CMakeFiles/Deodorarnt_Evaporator.dir/build.make
Deodorarnt_Evaporator.exe: CMakeFiles/Deodorarnt_Evaporator.dir/linklibs.rsp
Deodorarnt_Evaporator.exe: CMakeFiles/Deodorarnt_Evaporator.dir/objects1.rsp
Deodorarnt_Evaporator.exe: CMakeFiles/Deodorarnt_Evaporator.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Deodorarnt Evaporator\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable Deodorarnt_Evaporator.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\Deodorarnt_Evaporator.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Deodorarnt_Evaporator.dir/build: Deodorarnt_Evaporator.exe

.PHONY : CMakeFiles/Deodorarnt_Evaporator.dir/build

CMakeFiles/Deodorarnt_Evaporator.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Deodorarnt_Evaporator.dir\cmake_clean.cmake
.PHONY : CMakeFiles/Deodorarnt_Evaporator.dir/clean

CMakeFiles/Deodorarnt_Evaporator.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Deodorarnt Evaporator" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Deodorarnt Evaporator" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Deodorarnt Evaporator\cmake-build-debug" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Deodorarnt Evaporator\cmake-build-debug" "C:\Users\Patric\OneDrive\Dokument\GitHub\Codewars\C\7kyu\Deodorarnt Evaporator\cmake-build-debug\CMakeFiles\Deodorarnt_Evaporator.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Deodorarnt_Evaporator.dir/depend

