#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : ktextwidgets
Version  : 5.90.0
Release  : 45
URL      : https://download.kde.org/stable/frameworks/5.90/ktextwidgets-5.90.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.90/ktextwidgets-5.90.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.90/ktextwidgets-5.90.0.tar.xz.sig
Summary  : Advanced text editing widgets
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: ktextwidgets-lib = %{version}-%{release}
Requires: ktextwidgets-license = %{version}-%{release}
Requires: ktextwidgets-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcompletion-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : ki18n-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : sonnet-dev

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
%setup -q -n ktextwidgets-5.90.0
cd %{_builddir}/ktextwidgets-5.90.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642016496
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1642016496
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktextwidgets
cp %{_builddir}/ktextwidgets-5.90.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/ktextwidgets-5.90.0/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/ktextwidgets-5.90.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/ktextwidgets-5.90.0/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/ktextwidgets-5.90.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/ktextwidgets-5.90.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/ktextwidgets-5.90.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/ktextwidgets/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd
%find_lang ktextwidgets5

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KTextWidgets/KFind
/usr/include/KF5/KTextWidgets/KFindDialog
/usr/include/KF5/KTextWidgets/KPluralHandlingSpinBox
/usr/include/KF5/KTextWidgets/KRegExpEditorInterface
/usr/include/KF5/KTextWidgets/KReplace
/usr/include/KF5/KTextWidgets/KReplaceDialog
/usr/include/KF5/KTextWidgets/KRichTextEdit
/usr/include/KF5/KTextWidgets/KRichTextWidget
/usr/include/KF5/KTextWidgets/KTextEdit
/usr/include/KF5/KTextWidgets/kfind.h
/usr/include/KF5/KTextWidgets/kfinddialog.h
/usr/include/KF5/KTextWidgets/kpluralhandlingspinbox.h
/usr/include/KF5/KTextWidgets/kregexpeditorinterface.h
/usr/include/KF5/KTextWidgets/kreplace.h
/usr/include/KF5/KTextWidgets/kreplacedialog.h
/usr/include/KF5/KTextWidgets/krichtextedit.h
/usr/include/KF5/KTextWidgets/krichtextwidget.h
/usr/include/KF5/KTextWidgets/ktextedit.h
/usr/include/KF5/KTextWidgets/ktextwidgets_export.h
/usr/include/KF5/ktextwidgets_version.h
/usr/lib64/cmake/KF5TextWidgets/KF5TextWidgetsConfig.cmake
/usr/lib64/cmake/KF5TextWidgets/KF5TextWidgetsConfigVersion.cmake
/usr/lib64/cmake/KF5TextWidgets/KF5TextWidgetsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5TextWidgets/KF5TextWidgetsTargets.cmake
/usr/lib64/libKF5TextWidgets.so
/usr/lib64/qt5/mkspecs/modules/qt_KTextWidgets.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5TextWidgets.so.5
/usr/lib64/libKF5TextWidgets.so.5.90.0
/usr/lib64/qt5/plugins/designer/ktextwidgets5widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktextwidgets/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/ktextwidgets/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/ktextwidgets/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/ktextwidgets/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/ktextwidgets/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f ktextwidgets5.lang
%defattr(-,root,root,-)

