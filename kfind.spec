#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kfind
Version  : 24.12.0
Release  : 78
URL      : https://download.kde.org/stable/release-service/24.12.0/src/kfind-24.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.0/src/kfind-24.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.0/src/kfind-24.12.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kfilemetadata-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kfind-24.12.0
cd %{_builddir}/kfind-24.12.0
pushd ..
cp -a kfind-24.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735259234
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735259234
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kfind
cp %{_builddir}/kfind-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kfind/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kfind-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kfind/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kfind
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kfind
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
/usr/share/qlogging-categories6/kfind.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kfind/index.cache.bz2
/usr/share/doc/HTML/ca/kfind/index.docbook
/usr/share/doc/HTML/en/kfind/index.cache.bz2
/usr/share/doc/HTML/en/kfind/index.docbook
/usr/share/doc/HTML/es/kfind/index.cache.bz2
/usr/share/doc/HTML/es/kfind/index.docbook
/usr/share/doc/HTML/fr/kfind/index.cache.bz2
/usr/share/doc/HTML/fr/kfind/index.docbook
/usr/share/doc/HTML/it/kfind/index.cache.bz2
/usr/share/doc/HTML/it/kfind/index.docbook
/usr/share/doc/HTML/nl/kfind/index.cache.bz2
/usr/share/doc/HTML/nl/kfind/index.docbook
/usr/share/doc/HTML/sl/kfind/index.cache.bz2
/usr/share/doc/HTML/sl/kfind/index.docbook
/usr/share/doc/HTML/tr/kfind/index.cache.bz2
/usr/share/doc/HTML/tr/kfind/index.docbook
/usr/share/doc/HTML/uk/kfind/index.cache.bz2
/usr/share/doc/HTML/uk/kfind/index.docbook

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
/usr/share/man/sl/man1/kfind.1
/usr/share/man/sr/man1/kfind.1
/usr/share/man/sr@latin/man1/kfind.1
/usr/share/man/sv/man1/kfind.1
/usr/share/man/tr/man1/kfind.1
/usr/share/man/uk/man1/kfind.1

%files locales -f kfind.lang
%defattr(-,root,root,-)

