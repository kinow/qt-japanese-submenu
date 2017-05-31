# qt-japanese-submenu

See Krita bug [362967](https://bugs.kde.org/show_bug.cgi?id=362967) for a complete description of
the issue. In summary, there is one way to build a pop-up menu with an input field, where the
input field would not recognize is the local language was set to Japanese (and probably to other
languages too).

This repository contains an example application, to replicate the issue. There are actually two
applications, the initial Python PyQt application that was quickly created, and then a C++
and CMake application to report the issue to Qt.

TODO: list environment used for testing

