Summary:	ASCII-art graphics program
Summary(pl):	Program do tworzenia ASCII-artów
Name:		tetradraw
Version:	2.0.2
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://tentacle.dhs.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fix.patch
URL:		http://tentacle.dhs.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple program to create ASCII arts which can You use in fancylogin.

%description -l pl
Prosty program do tworzenia ASCII artów które mo¿esz wykorzystaæ w
programie fancylogin.

%prep
%setup -q
%patch -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS README TODO NEWS THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
