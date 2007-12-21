%define	module	WWW-Babelfish
%define	name	perl-%{module}
%define	version	0.16
%define	release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl extension for translation via Babelfish or Google
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/WWW/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:  perl-libwww-perl
BuildRequires:  perl(IO::String)
Buildarch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Perl interface to the WWW babelfish translation server.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOD
n
EOD
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/WWW
%{perl_vendorlib}/auto/WWW
%{_mandir}/*/*



