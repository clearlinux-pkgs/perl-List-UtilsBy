#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-UtilsBy
Version  : 0.11
Release  : 11
URL      : http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/List-UtilsBy-0.11.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/List-UtilsBy-0.11.tar.gz
Summary  : 'higher-order list utility functions'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-List-UtilsBy-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
List::UtilsBy - higher-order list utility functions
SYNOPSIS
use List::UtilsBy qw( nsort_by min_by );

use File::stat qw( stat );
my @files_by_age = nsort_by { stat($_)->mtime } @files;

my $shortest_name = min_by { length } @names;

%package dev
Summary: dev components for the perl-List-UtilsBy package.
Group: Development
Provides: perl-List-UtilsBy-devel = %{version}-%{release}

%description dev
dev components for the perl-List-UtilsBy package.


%package license
Summary: license components for the perl-List-UtilsBy package.
Group: Default

%description license
license components for the perl-List-UtilsBy package.


%prep
%setup -q -n List-UtilsBy-0.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-List-UtilsBy
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-List-UtilsBy/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/List/UtilsBy.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/List::UtilsBy.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-List-UtilsBy/LICENSE
