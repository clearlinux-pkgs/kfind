#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kfind
Version  : 18.08.0
Release  : 2
URL      : https://download.kde.org/stable/applications/18.08.0/src/kfind-18.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/18.08.0/src/kfind-18.08.0.tar.xz
Source99 : https://download.kde.org/stable/applications/18.08.0/src/kfind-18.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GFDL-1.3 GPL-2.0
Requires: kfind-bin
Requires: kfind-data
Requires: kfind-license
Requires: kfind-locales
Requires: kfind-man
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev qtbase-extras mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the kfind package.
Group: Binaries
Requires: kfind-data
Requires: kfind-license
Requires: kfind-man

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
Requires: kfind-man

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
%setup -q -n kfind-18.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535428609
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535428609
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kfind
cp COPYING %{buildroot}/usr/share/doc/kfind/COPYING
cp COPYING.DOC %{buildroot}/usr/share/doc/kfind/COPYING.DOC
cp src/COPYING %{buildroot}/usr/share/doc/kfind/src_COPYING
cp src/COPYING.DOC %{buildroot}/usr/share/doc/kfind/src_COPYING.DOC
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
/usr/share/icons/hicolor/16x16/apps/kfind.png
/usr/share/icons/hicolor/22x22/apps/kfind.png
/usr/share/icons/hicolor/32x32/apps/kfind.png
/usr/share/icons/hicolor/48x48/apps/kfind.png
/usr/share/icons/hicolor/64x64/apps/kfind.png
/usr/share/metainfo/org.kde.kfind.appdata.xml
/usr/share/xdg/kfind.categories

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
%defattr(-,root,root,-)
/usr/share/doc/kfind/COPYING
/usr/share/doc/kfind/COPYING.DOC
/usr/share/doc/kfind/src_COPYING
/usr/share/doc/kfind/src_COPYING.DOC

%files man
%defattr(-,root,root,-)
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

