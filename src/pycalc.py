#!/usr/bin/env python2
"""This module is part of PyCalc.

Copyright (C) 2016  Wilmin Ceballos <source@wilmin.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from calculator import Calculator

__version__ = '1.0'

if __name__ == '__main__':
    calc_app = Calculator()  # Create app instance with no parent
    calc_app.title('PyCalc')
    calc_app.mainloop()
