%define	upstream_name	 WWW-Babelfish
%define upstream_version 0.16
Name:		perl-%{upstream_name}
Version:	0.16
Release:	1

Summary:	Perl extension for translation via Babelfish or Google
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/D/DU/DURIST/WWW-Babelfish-0.16.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(HTML::TokeParser)
BuildRequires:	perl(IO::String)
BuildArch:	noarch

%description
Perl interface to the WWW babelfish translation server.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor <<EOD
n
EOD
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/WWW
%{perl_vendorlib}/auto/WWW
%{_mandir}/*/*


