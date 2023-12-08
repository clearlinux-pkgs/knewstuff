#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : knewstuff
Version  : 5.112.0
Release  : 67
URL      : https://download.kde.org/stable/frameworks/5.112/knewstuff-5.112.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.112/knewstuff-5.112.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.112/knewstuff-5.112.0.tar.xz.sig
Summary  : Support for downloading application assets from the network
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: knewstuff-bin = %{version}-%{release}
Requires: knewstuff-data = %{version}-%{release}
Requires: knewstuff-lib = %{version}-%{release}
Requires: knewstuff-license = %{version}-%{release}
Requires: knewstuff-locales = %{version}-%{release}
BuildRequires : attica-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : karchive-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kio-dev
BuildRequires : kirigami2-dev
BuildRequires : kitemviews-dev
BuildRequires : kpackage-dev
BuildRequires : kservice-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : syndication-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KNewStuff
Framework for downloading and sharing additional application data
## Introduction

%package bin
Summary: bin components for the knewstuff package.
Group: Binaries
Requires: knewstuff-data = %{version}-%{release}
Requires: knewstuff-license = %{version}-%{release}

%description bin
bin components for the knewstuff package.


%package data
Summary: data components for the knewstuff package.
Group: Data

%description data
data components for the knewstuff package.


%package dev
Summary: dev components for the knewstuff package.
Group: Development
Requires: knewstuff-lib = %{version}-%{release}
Requires: knewstuff-bin = %{version}-%{release}
Requires: knewstuff-data = %{version}-%{release}
Provides: knewstuff-devel = %{version}-%{release}
Requires: knewstuff = %{version}-%{release}

%description dev
dev components for the knewstuff package.


%package lib
Summary: lib components for the knewstuff package.
Group: Libraries
Requires: knewstuff-data = %{version}-%{release}
Requires: knewstuff-license = %{version}-%{release}

%description lib
lib components for the knewstuff package.


%package license
Summary: license components for the knewstuff package.
Group: Default

%description license
license components for the knewstuff package.


%package locales
Summary: locales components for the knewstuff package.
Group: Default

%description locales
locales components for the knewstuff package.


%prep
%setup -q -n knewstuff-5.112.0
cd %{_builddir}/knewstuff-5.112.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701999018
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
%cmake ..
make  %{?_smp_mflags}
popd
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
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1701999018
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knewstuff
cp %{_builddir}/knewstuff-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/knewstuff/ea97eb88ae53ec41e26f8542176ab986d7bc943a || :
cp %{_builddir}/knewstuff-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/knewstuff/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/knewstuff-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/knewstuff/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/knewstuff-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/knewstuff/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/knewstuff-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/knewstuff/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/knewstuff-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/knewstuff/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/knewstuff-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/knewstuff/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/knewstuff-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/knewstuff/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/knewstuff-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/knewstuff/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/knewstuff-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/knewstuff/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/knewstuff-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/knewstuff/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/knewstuff-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/knewstuff/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/knewstuff-%{version}/tests/README.tests.license %{buildroot}/usr/share/package-licenses/knewstuff/cf81cd36721334c927a5c0efd351d9b610632518 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang knewstuff5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/knewstuff-dialog
/usr/bin/knewstuff-dialog

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.knewstuff-dialog.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/_README.md
/usr/share/kf5/kmoretools/presets-kmoretools/angrysearch.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/catfish.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/com.obsproject.Studio.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/com.obsproject.Studio.png
/usr/share/kf5/kmoretools/presets-kmoretools/com.uploadedlobster.peek.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/ding.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/disk.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/filelight.svg
/usr/share/kf5/kmoretools/presets-kmoretools/fontinst.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/fontmatrix.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/fsearch.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/giggle.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/git-cola-folder-handler.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/git-cola-view-history.kmt-edition.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/git-cola.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/git-cola.svg
/usr/share/kf5/kmoretools/presets-kmoretools/gitg.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/gitg.png
/usr/share/kf5/kmoretools/presets-kmoretools/gitk.kmt-edition.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/gnome-search-tool.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/gparted.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/gparted.png
/usr/share/kf5/kmoretools/presets-kmoretools/gucharmap.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/hotshots.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/hotshots.png
/usr/share/kf5/kmoretools/presets-kmoretools/htop.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/kaption.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/kaption.desktop.TODO
/usr/share/kf5/kmoretools/presets-kmoretools/kding.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/org.gnome.clocks.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/org.kde.filelight.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/org.kde.kcharselect.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/org.kde.kdf.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/org.kde.kfind.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/org.kde.kmousetool.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/org.kde.ksysguard.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/org.kde.ksystemlog.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/org.kde.ktimer.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/org.kde.partitionmanager.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/org.kde.plasma.cuttlefish.kmt-edition.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/org.kde.spectacle.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/qgit.kmt-edition.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/shutter.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/shutter.desktop.TODO
/usr/share/kf5/kmoretools/presets-kmoretools/shutter.svg
/usr/share/kf5/kmoretools/presets-kmoretools/simplescreenrecorder.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/vokoscreenNG.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/vokoscreenNG.png
/usr/share/kf5/kmoretools/presets-kmoretools/xfce4-taskmanager.desktop
/usr/share/qlogging-categories5/knewstuff.categories
/usr/share/qlogging-categories5/knewstuff.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KMoreTools/KMoreTools
/usr/include/KF5/KMoreTools/KMoreToolsMenuFactory
/usr/include/KF5/KMoreTools/KMoreToolsPresets
/usr/include/KF5/KMoreTools/kmoretools.h
/usr/include/KF5/KMoreTools/kmoretoolsmenufactory.h
/usr/include/KF5/KMoreTools/kmoretoolspresets.h
/usr/include/KF5/KNewStuff3/KNS3/Button
/usr/include/KF5/KNewStuff3/KNS3/DownloadDialog
/usr/include/KF5/KNewStuff3/KNS3/DownloadManager
/usr/include/KF5/KNewStuff3/KNS3/DownloadWidget
/usr/include/KF5/KNewStuff3/KNS3/Entry
/usr/include/KF5/KNewStuff3/KNS3/KMoreTools
/usr/include/KF5/KNewStuff3/KNS3/KMoreToolsMenuFactory
/usr/include/KF5/KNewStuff3/KNS3/KMoreToolsPresets
/usr/include/KF5/KNewStuff3/KNS3/QtQuickDialogWrapper
/usr/include/KF5/KNewStuff3/KNS3/UploadDialog
/usr/include/KF5/KNewStuff3/KNS3/button.h
/usr/include/KF5/KNewStuff3/KNS3/downloaddialog.h
/usr/include/KF5/KNewStuff3/KNS3/downloadmanager.h
/usr/include/KF5/KNewStuff3/KNS3/downloadwidget.h
/usr/include/KF5/KNewStuff3/KNS3/entry.h
/usr/include/KF5/KNewStuff3/KNS3/kmoretools.h
/usr/include/KF5/KNewStuff3/KNS3/kmoretoolsmenufactory.h
/usr/include/KF5/KNewStuff3/KNS3/kmoretoolspresets.h
/usr/include/KF5/KNewStuff3/KNS3/knewstuff_export.h
/usr/include/KF5/KNewStuff3/KNS3/knewstuffaction.h
/usr/include/KF5/KNewStuff3/KNS3/qtquickdialogwrapper.h
/usr/include/KF5/KNewStuff3/KNS3/uploaddialog.h
/usr/include/KF5/KNewStuff3/KNSCore/Author
/usr/include/KF5/KNewStuff3/KNSCore/Cache
/usr/include/KF5/KNewStuff3/KNSCore/DownloadManager
/usr/include/KF5/KNewStuff3/KNSCore/Engine
/usr/include/KF5/KNewStuff3/KNSCore/EntryInternal
/usr/include/KF5/KNewStuff3/KNSCore/EntryWrapper
/usr/include/KF5/KNewStuff3/KNSCore/ErrorCode
/usr/include/KF5/KNewStuff3/KNSCore/Installation
/usr/include/KF5/KNewStuff3/KNSCore/ItemsModel
/usr/include/KF5/KNewStuff3/KNSCore/Provider
/usr/include/KF5/KNewStuff3/KNSCore/ProvidersModel
/usr/include/KF5/KNewStuff3/KNSCore/Question
/usr/include/KF5/KNewStuff3/KNSCore/QuestionListener
/usr/include/KF5/KNewStuff3/KNSCore/QuestionManager
/usr/include/KF5/KNewStuff3/KNSCore/Security
/usr/include/KF5/KNewStuff3/KNSCore/TagsFilterChecker
/usr/include/KF5/KNewStuff3/KNSCore/XmlLoader
/usr/include/KF5/KNewStuff3/KNSCore/author.h
/usr/include/KF5/KNewStuff3/KNSCore/cache.h
/usr/include/KF5/KNewStuff3/KNSCore/downloadmanager.h
/usr/include/KF5/KNewStuff3/KNSCore/engine.h
/usr/include/KF5/KNewStuff3/KNSCore/entryinternal.h
/usr/include/KF5/KNewStuff3/KNSCore/entrywrapper.h
/usr/include/KF5/KNewStuff3/KNSCore/errorcode.h
/usr/include/KF5/KNewStuff3/KNSCore/installation.h
/usr/include/KF5/KNewStuff3/KNSCore/itemsmodel.h
/usr/include/KF5/KNewStuff3/KNSCore/knewstuffcore_export.h
/usr/include/KF5/KNewStuff3/KNSCore/provider.h
/usr/include/KF5/KNewStuff3/KNSCore/providersmodel.h
/usr/include/KF5/KNewStuff3/KNSCore/question.h
/usr/include/KF5/KNewStuff3/KNSCore/questionlistener.h
/usr/include/KF5/KNewStuff3/KNSCore/questionmanager.h
/usr/include/KF5/KNewStuff3/KNSCore/security.h
/usr/include/KF5/KNewStuff3/KNSCore/tagsfilterchecker.h
/usr/include/KF5/KNewStuff3/KNSCore/xmlloader.h
/usr/include/KF5/KNewStuff3/KNSWidgets/Action
/usr/include/KF5/KNewStuff3/KNSWidgets/Button
/usr/include/KF5/KNewStuff3/KNSWidgets/action.h
/usr/include/KF5/KNewStuff3/KNSWidgets/button.h
/usr/include/KF5/KNewStuff3/KNSWidgets/knewstuffwidgets_export.h
/usr/include/KF5/KNewStuff3/knewstuff_version.h
/usr/include/KF5/KNewStuff3/knewstuffcore_version.h
/usr/include/KF5/KNewStuff3/knewstuffquick_version.h
/usr/include/KF5/KNewStuff3/kns3/button.h
/usr/include/KF5/KNewStuff3/kns3/downloaddialog.h
/usr/include/KF5/KNewStuff3/kns3/downloadmanager.h
/usr/include/KF5/KNewStuff3/kns3/downloadwidget.h
/usr/include/KF5/KNewStuff3/kns3/entry.h
/usr/include/KF5/KNewStuff3/kns3/kmoretools.h
/usr/include/KF5/KNewStuff3/kns3/kmoretoolsmenufactory.h
/usr/include/KF5/KNewStuff3/kns3/kmoretoolspresets.h
/usr/include/KF5/KNewStuff3/kns3/knewstuff_export.h
/usr/include/KF5/KNewStuff3/kns3/knewstuffaction.h
/usr/include/KF5/KNewStuff3/kns3/qtquickdialogwrapper.h
/usr/include/KF5/KNewStuff3/kns3/uploaddialog.h
/usr/include/KF5/KNewStuff3/knscore/author.h
/usr/include/KF5/KNewStuff3/knscore/cache.h
/usr/include/KF5/KNewStuff3/knscore/downloadmanager.h
/usr/include/KF5/KNewStuff3/knscore/engine.h
/usr/include/KF5/KNewStuff3/knscore/entryinternal.h
/usr/include/KF5/KNewStuff3/knscore/entrywrapper.h
/usr/include/KF5/KNewStuff3/knscore/errorcode.h
/usr/include/KF5/KNewStuff3/knscore/installation.h
/usr/include/KF5/KNewStuff3/knscore/itemsmodel.h
/usr/include/KF5/KNewStuff3/knscore/knewstuffcore_export.h
/usr/include/KF5/KNewStuff3/knscore/provider.h
/usr/include/KF5/KNewStuff3/knscore/providersmodel.h
/usr/include/KF5/KNewStuff3/knscore/question.h
/usr/include/KF5/KNewStuff3/knscore/questionlistener.h
/usr/include/KF5/KNewStuff3/knscore/questionmanager.h
/usr/include/KF5/KNewStuff3/knscore/security.h
/usr/include/KF5/KNewStuff3/knscore/tagsfilterchecker.h
/usr/include/KF5/KNewStuff3/knscore/xmlloader.h
/usr/include/KF5/KNewStuff3/knswidgets/action.h
/usr/include/KF5/KNewStuff3/knswidgets/button.h
/usr/include/KF5/KNewStuff3/knswidgets/knewstuffwidgets_export.h
/usr/lib64/cmake/KF5NewStuff/KF5NewStuffConfig.cmake
/usr/lib64/cmake/KF5NewStuff/KF5NewStuffConfigVersion.cmake
/usr/lib64/cmake/KF5NewStuff/KF5NewStuffTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5NewStuff/KF5NewStuffTargets.cmake
/usr/lib64/cmake/KF5NewStuffCore/KF5NewStuffCoreConfig.cmake
/usr/lib64/cmake/KF5NewStuffCore/KF5NewStuffCoreConfigVersion.cmake
/usr/lib64/cmake/KF5NewStuffCore/KF5NewStuffCoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5NewStuffCore/KF5NewStuffCoreTargets.cmake
/usr/lib64/cmake/KF5NewStuffQuick/KF5NewStuffQuickConfig.cmake
/usr/lib64/cmake/KF5NewStuffQuick/KF5NewStuffQuickConfigVersion.cmake
/usr/lib64/libKF5NewStuff.so
/usr/lib64/libKF5NewStuffCore.so
/usr/lib64/libKF5NewStuffWidgets.so
/usr/lib64/qt5/mkspecs/modules/qt_KNewStuff.pri
/usr/lib64/qt5/mkspecs/modules/qt_KNewStuffCore.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5NewStuff.so.5.112.0
/V3/usr/lib64/libKF5NewStuffCore.so.5.112.0
/V3/usr/lib64/libKF5NewStuffWidgets.so.5.112.0
/V3/usr/lib64/qt5/plugins/designer/knewstuffwidgets.so
/V3/usr/lib64/qt5/qml/org/kde/newstuff/libnewstuffqmlplugin.so
/usr/lib64/libKF5NewStuff.so.5
/usr/lib64/libKF5NewStuff.so.5.112.0
/usr/lib64/libKF5NewStuffCore.so.5
/usr/lib64/libKF5NewStuffCore.so.5.112.0
/usr/lib64/libKF5NewStuffWidgets.so.5
/usr/lib64/libKF5NewStuffWidgets.so.5.112.0
/usr/lib64/qt5/plugins/designer/knewstuffwidgets.so
/usr/lib64/qt5/qml/org/kde/newstuff/Action.qml
/usr/lib64/qt5/qml/org/kde/newstuff/Button.qml
/usr/lib64/qt5/qml/org/kde/newstuff/Dialog.qml
/usr/lib64/qt5/qml/org/kde/newstuff/DialogContent.qml
/usr/lib64/qt5/qml/org/kde/newstuff/DownloadItemsSheet.qml
/usr/lib64/qt5/qml/org/kde/newstuff/EntryDetails.qml
/usr/lib64/qt5/qml/org/kde/newstuff/NewStuffItem.qml
/usr/lib64/qt5/qml/org/kde/newstuff/NewStuffList.qml
/usr/lib64/qt5/qml/org/kde/newstuff/Page.qml
/usr/lib64/qt5/qml/org/kde/newstuff/QuestionAsker.qml
/usr/lib64/qt5/qml/org/kde/newstuff/UploadPage.qml
/usr/lib64/qt5/qml/org/kde/newstuff/libnewstuffqmlplugin.so
/usr/lib64/qt5/qml/org/kde/newstuff/private/ConditionalLoader.qml
/usr/lib64/qt5/qml/org/kde/newstuff/private/EntryCommentDelegate.qml
/usr/lib64/qt5/qml/org/kde/newstuff/private/EntryCommentsPage.qml
/usr/lib64/qt5/qml/org/kde/newstuff/private/EntryScreenshots.qml
/usr/lib64/qt5/qml/org/kde/newstuff/private/ErrorDisplayer.qml
/usr/lib64/qt5/qml/org/kde/newstuff/private/GridTileDelegate.qml
/usr/lib64/qt5/qml/org/kde/newstuff/private/MessageBoxSheet.qml
/usr/lib64/qt5/qml/org/kde/newstuff/private/Rating.qml
/usr/lib64/qt5/qml/org/kde/newstuff/private/Shadow.qml
/usr/lib64/qt5/qml/org/kde/newstuff/private/entrygriddelegates/BigPreviewDelegate.qml
/usr/lib64/qt5/qml/org/kde/newstuff/private/entrygriddelegates/FeedbackOverlay.qml
/usr/lib64/qt5/qml/org/kde/newstuff/private/entrygriddelegates/ThumbDelegate.qml
/usr/lib64/qt5/qml/org/kde/newstuff/private/entrygriddelegates/TileDelegate.qml
/usr/lib64/qt5/qml/org/kde/newstuff/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/knewstuff/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/knewstuff/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/knewstuff/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/knewstuff/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/knewstuff/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/knewstuff/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/knewstuff/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/knewstuff/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/knewstuff/cf81cd36721334c927a5c0efd351d9b610632518
/usr/share/package-licenses/knewstuff/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/knewstuff/ea97eb88ae53ec41e26f8542176ab986d7bc943a

%files locales -f knewstuff5.lang
%defattr(-,root,root,-)

