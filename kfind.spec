#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kfind
Version  : 23.04.0
Release  : 54
URL      : https://download.kde.org/stable/release-service/23.04.0/src/kfind-23.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.0/src/kfind-23.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.0/src/kfind-23.04.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: kfind-bin = %{version}-%{release}
Requires: kfind-data = %{version}-%{release}
Requires: kfind-license = %{version}-%{release}
Requires: kfind-locales = %{version}-%{release}
Requires: kfind-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kfilemetadata-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the kfind package.
Group: Binaries
Requires: kfind-data = %{version}-%{release}
Requires: kfind-license = %{version}-%{release}

%description bin
bin components for the kfind package.


%package data
Summary: data components for the kfind package.
Group: Data

%description data
data components for the kfind package.


%package doc
Summary: doc components for the kfind package.
Group: Documentation
Requires: kfind-man = %{version}-%{release}

%description doc
doc components for the kfind package.


%package license
Summary: license components for the kfind package.
Group: Default

%description license
license components for the kfind package.


%package locales
Summary: locales components for the kfind package.
Group: Default

%description locales
locales components for the kfind package.


%package man
Summary: man components for the kfind package.
Group: Default

%description man
man components for the kfind package.


%prep
%setup -q -n kfind-23.04.0
cd %{_builddir}/kfind-23.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682091122
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1682091122
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kfind
cp %{_builddir}/kfind-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kfind/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kfind-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kfind/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build
%make_install
popd
%find_lang kfind

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kfind

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kfind.desktop
/usr/share/icons/hicolor/128x128/apps/kfind.png
/usr/share/icons/hicolor/16x16/apps/kfind.png
/usr/share/icons/hicolor/22x22/apps/kfind.png
/usr/share/icons/hicolor/32x32/apps/kfind.png
/usr/share/icons/hicolor/48x48/apps/kfind.png
/usr/share/icons/hicolor/64x64/apps/kfind.png
/usr/share/icons/hicolor/scalable/apps/kfind.svgz
/usr/share/metainfo/org.kde.kfind.appdata.xml
/usr/share/qlogging-categories5/kfind.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kfind/index.cache.bz2
/usr/share/doc/HTML/ca/kfind/index.docbook
/usr/share/doc/HTML/de/kfind/index.cache.bz2
/usr/share/doc/HTML/de/kfind/index.docbook
/usr/share/doc/HTML/en/kfind/index.cache.bz2
/usr/share/doc/HTML/en/kfind/index.docbook
/usr/share/doc/HTML/es/kfind/index.cache.bz2
/usr/share/doc/HTML/es/kfind/index.docbook
/usr/share/doc/HTML/et/kfind/index.cache.bz2
/usr/share/doc/HTML/et/kfind/index.docbook
/usr/share/doc/HTML/fr/kfind/index.cache.bz2
/usr/share/doc/HTML/fr/kfind/index.docbook
/usr/share/doc/HTML/it/kfind/index.cache.bz2
/usr/share/doc/HTML/it/kfind/index.docbook
/usr/share/doc/HTML/lt/kfind/index.cache.bz2
/usr/share/doc/HTML/lt/kfind/index.docbook
/usr/share/doc/HTML/nl/kfind/index.cache.bz2
/usr/share/doc/HTML/nl/kfind/index.docbook
/usr/share/doc/HTML/pl/kfind/index.cache.bz2
/usr/share/doc/HTML/pl/kfind/index.docbook
/usr/share/doc/HTML/pt/kfind/index.cache.bz2
/usr/share/doc/HTML/pt/kfind/index.docbook
/usr/share/doc/HTML/pt_BR/kfind/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kfind/index.docbook
/usr/share/doc/HTML/ru/kfind/index.cache.bz2
/usr/share/doc/HTML/ru/kfind/index.docbook
/usr/share/doc/HTML/sr/kfind/index.cache.bz2
/usr/share/doc/HTML/sr/kfind/index.docbook
/usr/share/doc/HTML/sr@latin/kfind/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kfind/index.docbook
/usr/share/doc/HTML/sv/kfind/index.cache.bz2
/usr/share/doc/HTML/sv/kfind/index.docbook
/usr/share/doc/HTML/uk/kfind/index.cache.bz2
/usr/share/doc/HTML/uk/kfind/index.docbook
/usr/share/doc/HTML/zh_CN/kfind/index.cache.bz2
/usr/share/doc/HTML/zh_CN/kfind/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kfind/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kfind/3e8971c6c5f16674958913a94a36b1ea7a00ac46

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kfind.1
/usr/share/man/de/man1/kfind.1
/usr/share/man/es/man1/kfind.1
/usr/share/man/fr/man1/kfind.1
/usr/share/man/it/man1/kfind.1
/usr/share/man/lt/man1/kfind.1
/usr/share/man/man1/kfind.1
/usr/share/man/nb/man1/kfind.1
/usr/share/man/nl/man1/kfind.1
/usr/share/man/pl/man1/kfind.1
/usr/share/man/pt/man1/kfind.1
/usr/share/man/pt_BR/man1/kfind.1
/usr/share/man/ru/man1/kfind.1
/usr/share/man/sr/man1/kfind.1
/usr/share/man/sr@latin/man1/kfind.1
/usr/share/man/sv/man1/kfind.1
/usr/share/man/tr/man1/kfind.1
/usr/share/man/uk/man1/kfind.1

%files locales -f kfind.lang
%defattr(-,root,root,-)

