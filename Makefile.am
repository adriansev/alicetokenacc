#######################################################################
## Makefile.am for AliceTokenACC plugin
##
##
## Version info: $Id: Makefile.am,v 1.5 2006/07/24 07:38:57 dfeich Exp $
## Checked in by $Author: apeters $
#######################################################################

ACLOCAL_AMFLAGS = -I m4

lib_LTLIBRARIES = libXrdAliceTokenAcc.la

AM_CPPFLAGS = -I$(XROOTD_LOCATION)/include/xrootd -I$(OPENSSL_INCDIR) -I$(TKAUTHZ_INCDIR)

libXrdAliceTokenAcc_la_SOURCES = XrdAliceTokenAcc.cc XrdAliceTokenAcc.hh

libXrdAliceTokenAcc_la_LIBADD = -L$(XROOTD_LOCATION)/lib$(MARK64)/ -lXrdUtils -lXrdServer -L$(OPENSSL_LIBDIR)/ -lcrypto -L$(TKAUTHZ_LIBDIR)/ -lTokenAuthz

EXTRA_DIST = configure.ac configure bootstrap.sh xrootd-alicetokenacc.spec .authz

rpm:	dist
	cp $(DIST_ARCHIVES) /usr/src/redhat/SOURCES/
	rpmbuild -bb xrootd-alicetokenacc.spec

rpmnodist:
	cp $(DIST_ARCHIVES) /usr/src/redhat/SOURCES/
	rpmbuild -bb xrootd-alicetokenacc.spec


