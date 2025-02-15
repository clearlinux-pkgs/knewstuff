#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: e36a856
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : knewstuff
Version  : 6.11.0
Release  : 88
URL      : https://download.kde.org/stable/frameworks/6.11/knewstuff-6.11.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.11/knewstuff-6.11.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.11/knewstuff-6.11.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : Support for downloading application assets from the network
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: knewstuff-bin = %{version}-%{release}
Requires: knewstuff-data = %{version}-%{release}
Requires: knewstuff-lib = %{version}-%{release}
Requires: knewstuff-license = %{version}-%{release}
Requires: knewstuff-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n knewstuff-6.11.0
cd %{_builddir}/knewstuff-6.11.0
pushd ..
cp -a knewstuff-6.11.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739580985
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
export SOURCE_DATE_EPOCH=1739580985
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
%find_lang knewstuff6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/knewstuff-dialog6
/usr/bin/knewstuff-dialog6

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.knewstuff-dialog6.desktop
/usr/share/qlogging-categories6/knewstuff.categories
/usr/share/qlogging-categories6/knewstuff.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KNewStuff/knewstuff_version.h
/usr/include/KF6/KNewStuffCore/KNSCore/Author
/usr/include/KF6/KNewStuffCore/KNSCore/Cache
/usr/include/KF6/KNewStuffCore/KNSCore/CategoryMetadata
/usr/include/KF6/KNewStuffCore/KNSCore/EngineBase
/usr/include/KF6/KNewStuffCore/KNSCore/Entry
/usr/include/KF6/KNewStuffCore/KNSCore/ErrorCode
/usr/include/KF6/KNewStuffCore/KNSCore/ItemsModel
/usr/include/KF6/KNewStuffCore/KNSCore/Provider
/usr/include/KF6/KNewStuffCore/KNSCore/ProviderCore
/usr/include/KF6/KNewStuffCore/KNSCore/ProvidersModel
/usr/include/KF6/KNewStuffCore/KNSCore/Question
/usr/include/KF6/KNewStuffCore/KNSCore/QuestionListener
/usr/include/KF6/KNewStuffCore/KNSCore/QuestionManager
/usr/include/KF6/KNewStuffCore/KNSCore/ResultsStream
/usr/include/KF6/KNewStuffCore/KNSCore/SearchPreset
/usr/include/KF6/KNewStuffCore/KNSCore/SearchRequest
/usr/include/KF6/KNewStuffCore/KNSCore/TagsFilterChecker
/usr/include/KF6/KNewStuffCore/KNSCore/Transaction
/usr/include/KF6/KNewStuffCore/KNSCore/author.h
/usr/include/KF6/KNewStuffCore/KNSCore/cache.h
/usr/include/KF6/KNewStuffCore/KNSCore/categorymetadata.h
/usr/include/KF6/KNewStuffCore/KNSCore/enginebase.h
/usr/include/KF6/KNewStuffCore/KNSCore/entry.h
/usr/include/KF6/KNewStuffCore/KNSCore/errorcode.h
/usr/include/KF6/KNewStuffCore/KNSCore/itemsmodel.h
/usr/include/KF6/KNewStuffCore/KNSCore/knewstuffcore_export.h
/usr/include/KF6/KNewStuffCore/KNSCore/provider.h
/usr/include/KF6/KNewStuffCore/KNSCore/providercore.h
/usr/include/KF6/KNewStuffCore/KNSCore/providersmodel.h
/usr/include/KF6/KNewStuffCore/KNSCore/question.h
/usr/include/KF6/KNewStuffCore/KNSCore/questionlistener.h
/usr/include/KF6/KNewStuffCore/KNSCore/questionmanager.h
/usr/include/KF6/KNewStuffCore/KNSCore/resultsstream.h
/usr/include/KF6/KNewStuffCore/KNSCore/searchpreset.h
/usr/include/KF6/KNewStuffCore/KNSCore/searchrequest.h
/usr/include/KF6/KNewStuffCore/KNSCore/tagsfilterchecker.h
/usr/include/KF6/KNewStuffCore/KNSCore/transaction.h
/usr/include/KF6/KNewStuffWidgets/KNSWidgets/Action
/usr/include/KF6/KNewStuffWidgets/KNSWidgets/Button
/usr/include/KF6/KNewStuffWidgets/KNSWidgets/Dialog
/usr/include/KF6/KNewStuffWidgets/KNSWidgets/action.h
/usr/include/KF6/KNewStuffWidgets/KNSWidgets/button.h
/usr/include/KF6/KNewStuffWidgets/KNSWidgets/dialog.h
/usr/include/KF6/KNewStuffWidgets/KNSWidgets/knewstuffwidgets_export.h
/usr/lib64/cmake/KF6NewStuff/KF6NewStuffConfig.cmake
/usr/lib64/cmake/KF6NewStuff/KF6NewStuffConfigVersion.cmake
/usr/lib64/cmake/KF6NewStuff/KF6NewStuffTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6NewStuff/KF6NewStuffTargets.cmake
/usr/lib64/cmake/KF6NewStuffCore/KF6NewStuffCoreConfig.cmake
/usr/lib64/cmake/KF6NewStuffCore/KF6NewStuffCoreConfigVersion.cmake
/usr/lib64/cmake/KF6NewStuffCore/KF6NewStuffCoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6NewStuffCore/KF6NewStuffCoreTargets.cmake
/usr/lib64/libKF6NewStuffCore.so
/usr/lib64/libKF6NewStuffWidgets.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6NewStuffCore.so.6.11.0
/V3/usr/lib64/libKF6NewStuffWidgets.so.6.11.0
/V3/usr/lib64/qt6/plugins/designer/knewstuff6widgets.so
/V3/usr/lib64/qt6/qml/org/kde/newstuff/libnewstuffqmlplugin.so
/V3/usr/lib64/qt6/qml/org/kde/newstuff/private/libnewstuffqmlpluginprivate.so
/usr/lib64/libKF6NewStuffCore.so.6
/usr/lib64/libKF6NewStuffCore.so.6.11.0
/usr/lib64/libKF6NewStuffWidgets.so.6
/usr/lib64/libKF6NewStuffWidgets.so.6.11.0
/usr/lib64/qt6/plugins/designer/knewstuff6widgets.so
/usr/lib64/qt6/qml/org/kde/newstuff/Action.qml
/usr/lib64/qt6/qml/org/kde/newstuff/Button.qml
/usr/lib64/qt6/qml/org/kde/newstuff/Dialog.qml
/usr/lib64/qt6/qml/org/kde/newstuff/DialogContent.qml
/usr/lib64/qt6/qml/org/kde/newstuff/DownloadItemsSheet.qml
/usr/lib64/qt6/qml/org/kde/newstuff/EntryDetails.qml
/usr/lib64/qt6/qml/org/kde/newstuff/Page.qml
/usr/lib64/qt6/qml/org/kde/newstuff/QuestionAsker.qml
/usr/lib64/qt6/qml/org/kde/newstuff/UploadPage.qml
/usr/lib64/qt6/qml/org/kde/newstuff/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/newstuff/libnewstuffqmlplugin.so
/usr/lib64/qt6/qml/org/kde/newstuff/newstuffqmlplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/newstuff/private/ConditionalLoader.qml
/usr/lib64/qt6/qml/org/kde/newstuff/private/EntryCommentDelegate.qml
/usr/lib64/qt6/qml/org/kde/newstuff/private/EntryCommentsPage.qml
/usr/lib64/qt6/qml/org/kde/newstuff/private/EntryScreenshots.qml
/usr/lib64/qt6/qml/org/kde/newstuff/private/ErrorDisplayer.qml
/usr/lib64/qt6/qml/org/kde/newstuff/private/GridTileDelegate.qml
/usr/lib64/qt6/qml/org/kde/newstuff/private/Rating.qml
/usr/lib64/qt6/qml/org/kde/newstuff/private/Shadow.qml
/usr/lib64/qt6/qml/org/kde/newstuff/private/entrygriddelegates/BigPreviewDelegate.qml
/usr/lib64/qt6/qml/org/kde/newstuff/private/entrygriddelegates/FeedbackOverlay.qml
/usr/lib64/qt6/qml/org/kde/newstuff/private/entrygriddelegates/TileDelegate.qml
/usr/lib64/qt6/qml/org/kde/newstuff/private/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/newstuff/private/libnewstuffqmlpluginprivate.so
/usr/lib64/qt6/qml/org/kde/newstuff/private/newstuffqmlpluginprivate.qmltypes
/usr/lib64/qt6/qml/org/kde/newstuff/private/qmldir
/usr/lib64/qt6/qml/org/kde/newstuff/qmldir

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
/usr/share/package-licenses/knewstuff/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/knewstuff/ea97eb88ae53ec41e26f8542176ab986d7bc943a

%files locales -f knewstuff6.lang
%defattr(-,root,root,-)

