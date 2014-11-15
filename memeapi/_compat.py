import sys

_ver = sys.version_info

is_py2 = (_ver[0] == 2)
is_py3 = (_ver[0] == 3)

if is_py3:
    string_types = (str,)
    integer_types = (int,)
elif is_py2:
    string_types = (str, unicode)
    integer_types = (int, long)
