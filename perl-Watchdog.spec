#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Watchdog
Summary:	Watchdog - set of watchdog modules
Summary(pl):	Watchdog - zbiór modu³ów do monitoringu
Name:		perl-Watchdog
Version:	0.10
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	63e684be05307a8cd148d9020d62b99c
BuildRequires:	perl-Alias
BuildRequires:	perl-Proc-ProcessTable
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Watchdog::Process, Watchdog::HTTP and Watchdog::Mysql are classes for
monitoring whether a process, HTTP server or MySQL server respectively
is functioning.

%description -l pl
Watchdog::Process, Watchdog::HTTP i Watchdog::Mysql s± modu³ami
s³u¿±cymi do monitorowania pracy procesów, serwera WWW lub MySQL.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README etc/watchdog.conf
%dir %{perl_vendorlib}/Watchdog
%{perl_vendorlib}/Watchdog/*.pm
%{_mandir}/man3/*
