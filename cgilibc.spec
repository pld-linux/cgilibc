# the true package name is "cgilib", but it was already taken by other library
%define	realname	cgilib
Summary:	Common Gateway Interface library
Summary(pl):	Biblioteka CGI (Common Gateway Interface)
Name:		cgilibc
Version:	0.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ibiblio.org/pub/Linux/libs/%{realname}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
Patch1:		%{name}-fix.patch
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common Gateway Interface library written in pure C by Martin Schultze.
Original project name was "cgilib", but we must have renamed it
because of name conflict with existing cgilib package (completely
different CGI library in C++ from http://cgilib.sourceforge.net/).

%description -l pl
Biblioteka CGI (Common Gateway Interface) napisana w czystym C przez
Martina Schultze. Oryginalna nazwa projektu to "cgilib", ale
musieli¶my j± zmieniæ z powodu konfliktu z ju¿ istniej±cym pakietem
cgilib (ca³kowicie inn± bibliotek± CGI w C++ z
http://cgilib.sourceforge.net/).

%package devel
Summary:	cgilib header files
Summary(pl):	Pliki nag³ówkowe cgilib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
cgilib header files.

%description devel -l pl
Pliki nag³ówkowe cgilib.

%package static
Summary:	Static version of cgilib
Summary(pl):	Statyczna wersja cgilib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of cgilib.

%description static -l pl
Statyczna wersja cgilib.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I."

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS cookies.txt readme
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/cgilibc
%{_mandir}/man[35]/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
