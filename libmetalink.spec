#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	static_libs	# don't build static libraries

Summary:	Metalink library written in C
Name:		libmetalink
Version:	0.1.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://launchpad.net/libmetalink/trunk/packagingfix/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	e60ea56d910ebfe4c303808db497e92a
URL:		https://launchpad.net/libmetalink
%{?with_tests:BuildRequires:	CUnit-devel}
BuildRequires:	expat-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmetalink is a Metalink C library. It adds Metalink functionality
such as parsing Metalink XML files to programs written in C.

%package	devel
Summary:	Files needed for developing with %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description	devel
Files needed for building applications with libmetalink.

%prep
%setup -q

%build
%configure \
	--disable-static \

%{__make}

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmetalink.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/libmetalink.so.*.*.*
%ghost %{_libdir}/libmetalink.so.3

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/metalink
%{_includedir}/metalink/metalink_error.h
%{_includedir}/metalink/metalink.h
%{_includedir}/metalink/metalink_parser.h
%{_includedir}/metalink/metalink_types.h
%{_includedir}/metalink/metalinkver.h
%{_libdir}/libmetalink.so
%{_pkgconfigdir}/libmetalink.pc
%{_mandir}/man3/metalink_*.3*
