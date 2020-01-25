#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# interactive

%define		pdir	Resources
Summary:	Resources - handling application defaults in Perl
Summary(pl.UTF-8):	Resources - obsługiwanie wartości domyślnych w Perlu
Name:		perl-Resources
Version:	1.04
Release:	13
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Resources/Resources-%{version}.tar.gz
# Source0-md5:	59c1e2bcfddecf6ca0c55031c482042d
URL:		http://search.cpan.org/dist/Resources/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Resources.pm is Perl package used to specify configuration (defaults,
...) parameters for Perl applications, pretty much in the same way as
X Window System does. It implements dynamical inheritance of defaults
(both values and names) through subclassing, parameter loading from
files, runtime parameter viewing and editing. The package contains an
extensive documentation in POD format, to which you are kindly
referred.

%description -l pl.UTF-8
Resources.pm to pakiet Perla używany do przekazywania konfiguracji
(domyślnych wartości) do aplikacji perlowych w podobny sposób, jak
robi to system X Window. Moduł ma zaimplementowane dynamiczne
dziedziczenie wielkości domyślnych (zarówno wartości, jak i nazw)
poprzez podklasy, wczytywanie parametrów z plików, przeglądanie i
edycję parametrów w czasie działania. Pakiet zawiera obszerną
dokumentację.

%prep
%setup -q -n Resources-%{version}

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
%doc Changes README
%{perl_vendorlib}/Resources.pm
%{_mandir}/man3/*
