%include	/usr/lib/rpm/macros.perl
Summary:	Resources - handling application defaults in Perl.
Name:		perl-Resources
Version:	1.04
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Resources/Resources-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Resources.pm is Perl package used to specify configuration (defaults,
...)  parameters for Perl applications, pretty much in the same way as
XWindows does.  It implements dynamical inheritance of defaults (both
values and names) through subclassing, parameter loading from files,
runtime parameter viewing and editing. The package contains an extensive
documentation in POD format, to which you are kindly referred.

%prep
%setup -q -n Resources-%{version}

%build
perl Makefile.PL
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
