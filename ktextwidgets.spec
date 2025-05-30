#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v26
# autospec commit: 99a7985
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : ktextwidgets
Version  : 6.14.0
Release  : 94
URL      : https://download.kde.org/stable/frameworks/6.14/ktextwidgets-6.14.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.14/ktextwidgets-6.14.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.14/ktextwidgets-6.14.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : Advanced text editing widgets
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: ktextwidgets-lib = %{version}-%{release}
Requires: ktextwidgets-license = %{version}-%{release}
Requires: ktextwidgets-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kcompletion-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : qt6base-dev
BuildRequires : sonnet-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KTextWidgets
Text editing widgets
## Introduction
KTextWidgets provides widgets for displaying and editing text. It supports
rich text as well as plain text.

%package dev
Summary: dev components for the ktextwidgets package.
Group: Development
Requires: ktextwidgets-lib = %{version}-%{release}
Provides: ktextwidgets-devel = %{version}-%{release}
Requires: ktextwidgets = %{version}-%{release}

%description dev
dev components for the ktextwidgets package.


%package lib
Summary: lib components for the ktextwidgets package.
Group: Libraries
Requires: ktextwidgets-license = %{version}-%{release}

%description lib
lib components for the ktextwidgets package.


%package license
Summary: license components for the ktextwidgets package.
Group: Default

%description license
license components for the ktextwidgets package.


%package locales
Summary: locales components for the ktextwidgets package.
Group: Default

%description locales
locales components for the ktextwidgets package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n ktextwidgets-6.14.0
cd %{_builddir}/ktextwidgets-6.14.0
pushd ..
cp -a ktextwidgets-6.14.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747157781
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
export SOURCE_DATE_EPOCH=1747157781
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktextwidgets
cp %{_builddir}/ktextwidgets-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/ktextwidgets-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/ktextwidgets-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/ktextwidgets-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/ktextwidgets-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/ktextwidgets-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/ktextwidgets-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/e458941548e0864907e654fa2e192844ae90fc32 || :
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
%find_lang ktextwidgets6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KTextWidgets/KFind
/usr/include/KF6/KTextWidgets/KFindDialog
/usr/include/KF6/KTextWidgets/KPluralHandlingSpinBox
/usr/include/KF6/KTextWidgets/KReplace
/usr/include/KF6/KTextWidgets/KReplaceDialog
/usr/include/KF6/KTextWidgets/KRichTextEdit
/usr/include/KF6/KTextWidgets/KRichTextWidget
/usr/include/KF6/KTextWidgets/KTextEdit
/usr/include/KF6/KTextWidgets/kfind.h
/usr/include/KF6/KTextWidgets/kfinddialog.h
/usr/include/KF6/KTextWidgets/kpluralhandlingspinbox.h
/usr/include/KF6/KTextWidgets/kreplace.h
/usr/include/KF6/KTextWidgets/kreplacedialog.h
/usr/include/KF6/KTextWidgets/krichtextedit.h
/usr/include/KF6/KTextWidgets/krichtextwidget.h
/usr/include/KF6/KTextWidgets/ktextedit.h
/usr/include/KF6/KTextWidgets/ktextwidgets_export.h
/usr/include/KF6/KTextWidgets/ktextwidgets_version.h
/usr/lib64/cmake/KF6TextWidgets/KF6TextWidgetsConfig.cmake
/usr/lib64/cmake/KF6TextWidgets/KF6TextWidgetsConfigVersion.cmake
/usr/lib64/cmake/KF6TextWidgets/KF6TextWidgetsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6TextWidgets/KF6TextWidgetsTargets.cmake
/usr/lib64/libKF6TextWidgets.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6TextWidgets.so.6.14.0
/V3/usr/lib64/qt6/plugins/designer/ktextwidgets6widgets.so
/usr/lib64/libKF6TextWidgets.so.6
/usr/lib64/libKF6TextWidgets.so.6.14.0
/usr/lib64/qt6/plugins/designer/ktextwidgets6widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktextwidgets/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/ktextwidgets/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/ktextwidgets/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/ktextwidgets/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/ktextwidgets/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f ktextwidgets6.lang
%defattr(-,root,root,-)

