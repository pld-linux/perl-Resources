%include	/usr/lib/rpm/macros.perl
Summary:	Resources - handling application defaults in Perl
Summary(pl):	Resources - obs³ugiwanie warto¶ci domy¶lnych w Perlu
Name:		perl-Resources
Version:	1.04
Release:	11
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Resources/Resources-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Resources.pm is Perl package used to specify configuration (defaults,
...)  parameters for Perl applications, pretty much in the same way as
X Window System does.  It implements dynamical inheritance of defaults
(both values and names) through subclassing, parameter loading from
files, runtime parameter viewing and editing. The package contains an
extensive documentation in POD format, to which you are kindly
referred.

%description -l pl
Resources.pm to pakiet Perla u¿ywany do przekazywania konfiguracji
(domy¶lnych warto¶ci) do aplikacji perlowych w podobny sposób, jak
robi to system X Window. Modu³ ma zaimplementowane dynamiczne
dziedziczenie wielko¶ci domy¶lnych (zarówno warto¶ci, jak i nazw)
poprzez podklasy, wczytywanie parametrów z plików, przegl±danie i
edycjê parametrów w czasie dzia³ania. Pakiet zawiera obszern±
dokumentacjê.

%prep
%setup -q -n Resources-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Resources.pm
%{_mandir}/man3/*
