
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Watchdog
Summary:	Watchdog - set of watchdog modules
Summary(pl):	Watchdog - zbiór modu³ów do monitoringu.
Name:		perl-Watchdog
Version:	0.10
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	63e684be05307a8cd148d9020d62b99c
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Alias
BuildRequires:	perl-Proc-ProcessTable
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Watchdog::Process, Watchdog::HTTP and Watchdog::Mysql are classes for
monitoring whether a process, http server or mysql server respectively
is functioning.

%description -l pl
Watchdog::Process, Watchdog::HTTP and Watchdog::Mysql sa modu³ami s³u¿acymi
do monitorowania pracy procesów, serwera www lub mysql.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Watchdog
%{perl_vendorlib}/Watchdog/*.pm
%{_mandir}/man3/*
