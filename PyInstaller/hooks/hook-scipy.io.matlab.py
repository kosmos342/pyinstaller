#-----------------------------------------------------------------------------
# Copyright (c) 2013-2017, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


# Module scipy.io.matlab allows to parse matlab files.
# The hidden import is necessary for SciPy 0.11+.
hiddenimports = ['scipy.io.matlab.streams']
