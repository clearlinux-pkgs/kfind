#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kfind
Version  : 19.12.2
Release  : 20
URL      : https://download.kde.org/stable/release-service/19.12.2/src/kfind-19.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.2/src/kfind-19.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.2/src/kfind-19.12.2.tar.xz.sig
Summary  : Find Files/Folders
Group    : Development/Tools
License  : GFDL-1.2 GFDL-1.3 GPL-2.0
Requires: kfind-bin = %{version}-%{release}
Requires: kfind-data = %{version}-%{release}
Requires: kfind-license = %{version}-%{release}
Requires: kfind-locales = %{version}-%{release}
Requires: kfind-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kfilemetadata-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kfind-19.12.2
cd %{_builddir}/kfind-19.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581020400
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581020400
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kfind
cp %{_builddir}/kfind-19.12.2/COPYING %{buildroot}/usr/share/package-licenses/kfind/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kfind-19.12.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/kfind/e1d31e42d2a477d6def889000aa8ffc251f2354c
cp %{_builddir}/kfind-19.12.2/src/COPYING %{buildroot}/usr/share/package-licenses/kfind/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/kfind-19.12.2/src/COPYING.DOC %{buildroot}/usr/share/package-licenses/kfind/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
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
/usr/share/doc/HTML/sv/kfind/index.cache.bz2
/usr/share/doc/HTML/sv/kfind/index.docbook
/usr/share/doc/HTML/uk/kfind/index.cache.bz2
/usr/share/doc/HTML/uk/kfind/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kfind/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kfind/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/kfind/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
/usr/share/package-licenses/kfind/e1d31e42d2a477d6def889000aa8ffc251f2354c

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
/usr/share/man/sv/man1/kfind.1
/usr/share/man/uk/man1/kfind.1

%files locales -f kfind.lang
%defattr(-,root,root,-)

