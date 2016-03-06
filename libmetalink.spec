#
# Conditional build:
%bcond_with	tests		# perform "make check"
%bcond_without	static_libs	# don't build static library

Summary:	Metalink library written in C
Summary(pl.UTF-8):	Biblioteka obsługi plików Metalink napisana w C
Name:		libmetalink
Version:	0.1.3
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://launchpad.net/libmetalink/trunk/%{name}-%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	f2c097557e2487313cd0be62d55952de
URL:		https://launchpad.net/libmetalink
%{?with_tests:BuildRequires:	CUnit-devel >= 2.1}
BuildRequires:	expat-devel >= 1:2.1.0
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	expat >= 1:2.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmetalink is a Metalink C library. It adds Metalink functionality
such as parsing Metalink XML files to programs written in C.

%description -l pl.UTF-8
libmetalink to biblioteka Metalink dla języka C. Dodaje funkcjonalność
Metalink, taką jak analiza plików XML Metalink do programów napisanych
w C.

%package devel
Summary:	Files needed for developing with libmetalink
Summary(pl.UTF-8):	Pliki niezbędne do tworzenia aplikacji z użyciem libmetalink
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	expat-devel >= 1:2.1.0

%description devel
Files needed for building applications with libmetalink.

%description devel -l pl.UTF-8
Pliki niezbędne do tworzenia aplikacji z użyciem libmetalink.

%package static
Summary:	Static libmetalink library
Summary(pl.UTF-8):	Statyczna biblioteka libmetalink
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmetalink library.

%description static -l pl.UTF-8
Statyczna biblioteka libmetalink.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}

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
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmetalink.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmetalink.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmetalink.so
%dir %{_includedir}/metalink
%{_includedir}/metalink/metalink_error.h
%{_includedir}/metalink/metalink.h
%{_includedir}/metalink/metalink_parser.h
%{_includedir}/metalink/metalink_types.h
%{_includedir}/metalink/metalinkver.h
%{_pkgconfigdir}/libmetalink.pc
%{_mandir}/man3/metalink_*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmetalink.a
%endif
