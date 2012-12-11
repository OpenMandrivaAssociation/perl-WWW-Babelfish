%define	upstream_name	 WWW-Babelfish
%define	upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl extension for translation via Babelfish or Google
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(HTML::TokeParser)
BuildRequires:	perl(IO::String)
BuildArch:	noarch

%description
Perl interface to the WWW babelfish translation server.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 409020
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.16-3mdv2009.0
+ Revision: 242149
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.16-1mdv2008.0
+ Revision: 20753
- 0.16


* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.15-2mdv2007.0
+ Revision: 73442
-  Fix  BuildRequires
- Add BuildRequires
- import perl-WWW-Babelfish-0.15-1mdv2007.0

* Sat Jun 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2007.0
- New version 0.15

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2007.0
- New release 0.14
- better summary
- better description
- enable tests

* Sat Apr 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.13-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Fri Aug 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdk
- new version
- fix sources url for rpmbuildupdate

* Tue Apr 20 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.12-1mdk
- 0.12

