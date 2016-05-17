%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%if %{?fedora}%{!?fedora:0} >= 21 || %{?rhel}%{!?rhel:0} >= 7
%global use_systemd 1
%else
%global use_systemd 0
%endif

Summary:	Alice Token Authorization Acc plugin
Name:		xrootd-alicetokenacc
Version:	1.2.5
Epoch:		1
Release:	1%{?dist}
License:	none
Group:		System Environment/Daemons

Source0: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%ifarch x86_64
  %define __lib lib64
%else
  %define __lib lib
%endif

%define __prefix /usr
%define __libdir /usr/%{__lib}
%define __incdir /usr/include
%define __xrootddir /usr
%define __tkauthzlibdir /usr/%{__lib}
%define __tkauthzincdir /usr/include
%define __sslincdir /usr/include

Requires: xrootd-server >= 4.0.0 , xrootd-client >= 4.0.0 , tokenauthz , openssl

%pretrans
#%global __xrootd_user %(find /home -maxdepth 2 -type f -name .xrootd_user | awk -F/ '{print $3}'| egrep '.*' || echo root)
#%global __user_home %( [[ "$_xrootd_user" == "root" ]] && echo "/root" || echo "/home/$user")

%description
An authorization plugin for xrootd using the Alice Token authorization envelope.

%prep
%setup -q

%build
./configure --prefix=%{__prefix} --libdir=%{__libdir} --includedir=%{__incdir} --with-xrootd-location=%{__xrootddir} --with-tkauthz-libdir=%{__tkauthzlibdir} --with-tkauthz-incdir=%{__tkauthzincdir} -with-openssl-incdir=%{__sslincdir}
make %{?_smp_mflags}

make install DESTDIR=$RPM_BUILD_ROOT

###mkdir -p $RPM_BUILD_ROOT/etc/grid-security/xrootd/
###cp -av .authz/xrootd/* $RPM_BUILD_ROOT/etc/grid-security/xrootd

find $RPM_BUILD_ROOT \( -type f -o -type l \) -print | sed "s#^$RPM_BUILD_ROOT/*#/#" > RPM-FILE-LIST

%clean
rm -rf $RPM_BUILD_ROOT

%files -f RPM-FILE-LIST
%defattr(-,root,root,-)

%doc

%post
##mv /etc/grid-security/xrootd/TkAuthz.Authorization %{__user_home}/.authz/xrootd/TkAuthz.Authorization
##mv /etc/grid-security/xrootd/privkey.pem %{__user_home}/.authz/xrootd/privkey.pem
##mv /etc/grid-security/xrootd/pubkey.pem %{__user_home}/.authz/xrootd/pubkey.pem

##%attr(644, %{__xrootd_user}, %{__xrootd_user}) %{__user_home}/.authz/xrootd/TkAuthz.Authorization
##%attr(400, %{__xrootd_user}, %{__xrootd_user}) %{__user_home}/.authz/xrootd/privkey.pem
##%attr(400, %{__xrootd_user}, %{__xrootd_user}) %{__user_home}/.authz/xrootd/pubkey.pem


%changelog
* Fri Aug 22 2008 root <root@pcitsmd01.cern.ch> - alicetokenacc-1
- Initial build.
