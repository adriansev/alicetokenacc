#!/bin/bash
libtoolize --copy --force
aclocal
automake -acf
autoconf

