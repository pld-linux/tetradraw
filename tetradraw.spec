Summary:	ASCII-art graphics program.
Summary(pl):	Program do tworzenia ASCII-artów.
Name:		tetradraw
Version:	2.0.2
Release:	1
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
License:	GPL
Source0:	http://tentacle.dhs.org/%{name}-%{version}.tar.gz
URL:		http://tentacle.dhs.org
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple program to create ASCII arts which can You use in fancylogin.

%description -l pl
Prosty program do tworzenia ASCII artów które mo¿esz wykorzystaæ w
programie fancylogin.

%prep
%setup  -q

%build
%configure 
%{__make} CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g} -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS README TODO NEWS THANKS 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
