# the true package name is "cgilib", but it was already taken by other library
%define	realname	cgilib
Summary:	Common Gateway Interface library
Summary(pl.UTF-8):	Biblioteka CGI (Common Gateway Interface)
Name:		cgilibc
Version:	0.7
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.infodrom.org/projects/cgilib/download/%{realname}-%{version}.tar.gz
# Source0-md5:	2c7053f58dfb06f7a80a112797ed7e86
Patch0:		%{name}-suffix.patch
URL:		http://www.infodrom.org/projects/cgilib/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common Gateway Interface library written in pure C by Martin Schultze.
Original project name was "cgilib", but we must have renamed it
because of name conflict with existing cgilib package (completely
different CGI library in C++ from http://cgilib.sourceforge.net/).

%description -l pl.UTF-8
Biblioteka CGI (Common Gateway Interface) napisana w czystym C przez
Martina Schultze. Oryginalna nazwa projektu to "cgilib", ale
musieliśmy ją zmienić z powodu konfliktu z już istniejącym pakietem
cgilib (całkowicie inną biblioteką CGI w C++ z
http://cgilib.sourceforge.net/).

%package devel
Summary:	cgilib header files
Summary(pl.UTF-8):	Pliki nagłówkowe cgilib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
cgilib header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe cgilib.

%package static
Summary:	Static version of cgilib
Summary(pl.UTF-8):	Statyczna wersja cgilib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of cgilib.

%description static -l pl.UTF-8
Statyczna wersja cgilib.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# examples - include as source, not binaries
%{__rm} $RPM_BUILD_ROOT%{_bindir}/{cgitest,jumpto}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p cgitest.c jumpto.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README cookies.txt
%attr(755,root,root) %{_libdir}/libcgic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcgic.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcgic.so
%{_libdir}/libcgic.la
%{_includedir}/cgilibc
%{_mandir}/man3/cgi*.3*
%{_mandir}/man5/cgi.5*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libcgic.a
