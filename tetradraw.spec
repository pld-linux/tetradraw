Summary:	ASCII-art graphics program
Summary(pl.UTF-8):	Program do tworzenia ASCII-artów
Name:		tetradraw
Version:	2.0.3
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://tentacle.dhs.org/%{name}-%{version}.tar.gz
# Source0-md5:	f3bb1802ff9e27d80c96225323715139
Patch0:		%{name}-am_fix.patch
URL:		http://tentacle.dhs.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple program to create ASCII arts which can You use in fancylogin.

%description -l pl.UTF-8
Prosty program do tworzenia ASCII artów które możesz wykorzystać w
programie fancylogin.

%prep
%setup -q
%patch -P0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO NEWS THANKS
%attr(755,root,root) %{_bindir}/*
