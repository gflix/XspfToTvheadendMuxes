#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([xspf-to-tvheadend-muxes], [0.0.1], [felix.mellmann@gmail.com])
AC_CONFIG_MACRO_DIR([m4])

AM_INIT_AUTOMAKE()

# Checks for programs.
AM_PATH_PYTHON([3.6])

# Checks for libraries.

# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.

AC_DEFINE_DIR([LIBDIR], [libdir], [Path at which library files are placed to.])

AC_CONFIG_FILES([
    Makefile
    src/Makefile
    src/xspf-to-tvheadend-muxes:src/xspf-to-tvheadend-muxes.py
])
AC_OUTPUT
