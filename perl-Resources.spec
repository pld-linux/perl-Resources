%include	/usr/lib/rpm/macros.perl
Summary:	Resources perl module
Summary(pl):	Modu³ perla Resources
Name:		perl-Resources
Version:	1.04
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Resources/Resources-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Resources perl module.

%description -l pl
Modu³ perla Resources.

%prep
%setup -q -n Resources-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Resources.pm
%{_mandir}/man3/*
