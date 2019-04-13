#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : knewstuff
Version  : 5.57.0
Release  : 13
URL      : https://download.kde.org/stable/frameworks/5.57/knewstuff-5.57.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.57/knewstuff-5.57.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.57/knewstuff-5.57.0.tar.xz.sig
Summary  : Support for downloading application assets from the network
Group    : Development/Tools
License  : LGPL-2.1
Requires: knewstuff-data = %{version}-%{release}
Requires: knewstuff-lib = %{version}-%{release}
Requires: knewstuff-license = %{version}-%{release}
Requires: knewstuff-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kirigami2-dev
BuildRequires : qtbase-dev mesa-dev

%description
# KNewStuff
Framework for downloading and sharing additional application data
## Introduction

%package data
Summary: data components for the knewstuff package.
Group: Data

%description data
data components for the knewstuff package.


%package dev
Summary: dev components for the knewstuff package.
Group: Development
Requires: knewstuff-lib = %{version}-%{release}
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
%setup -q -n knewstuff-5.57.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555199189
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555199189
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knewstuff
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/knewstuff/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang knewstuff5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kf5/kmoretools/presets-kmoretools/_README.md
/usr/share/kf5/kmoretools/presets-kmoretools/angrysearch.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/catfish.desktop
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
/usr/share/kf5/kmoretools/presets-kmoretools/vokoscreen.desktop
/usr/share/kf5/kmoretools/presets-kmoretools/vokoscreen.png
/usr/share/kf5/kmoretools/presets-kmoretools/xfce4-taskmanager.desktop
/usr/share/kf5/knewstuff/pics/thumb_frame.png
/usr/share/xdg/knewstuff.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KNewStuff3/KNS3/Button
/usr/include/KF5/KNewStuff3/KNS3/DownloadDialog
/usr/include/KF5/KNewStuff3/KNS3/DownloadManager
/usr/include/KF5/KNewStuff3/KNS3/DownloadWidget
/usr/include/KF5/KNewStuff3/KNS3/Entry
/usr/include/KF5/KNewStuff3/KNS3/KMoreTools
/usr/include/KF5/KNewStuff3/KNS3/KMoreToolsMenuFactory
/usr/include/KF5/KNewStuff3/KNS3/KMoreToolsPresets
/usr/include/KF5/KNewStuff3/KNS3/UploadDialog
/usr/include/KF5/KNewStuff3/KNSCore/Author
/usr/include/KF5/KNewStuff3/KNSCore/Cache
/usr/include/KF5/KNewStuff3/KNSCore/DownloadManager
/usr/include/KF5/KNewStuff3/KNSCore/Engine
/usr/include/KF5/KNewStuff3/KNSCore/EntryInternal
/usr/include/KF5/KNewStuff3/KNSCore/ErrorCode
/usr/include/KF5/KNewStuff3/KNSCore/Installation
/usr/include/KF5/KNewStuff3/KNSCore/ItemsModel
/usr/include/KF5/KNewStuff3/KNSCore/Provider
/usr/include/KF5/KNewStuff3/KNSCore/Question
/usr/include/KF5/KNewStuff3/KNSCore/QuestionListener
/usr/include/KF5/KNewStuff3/KNSCore/QuestionManager
/usr/include/KF5/KNewStuff3/KNSCore/Security
/usr/include/KF5/KNewStuff3/KNSCore/TagsFilterChecker
/usr/include/KF5/KNewStuff3/KNSCore/XmlLoader
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
/usr/include/KF5/KNewStuff3/kns3/uploaddialog.h
/usr/include/KF5/KNewStuff3/knscore/author.h
/usr/include/KF5/KNewStuff3/knscore/cache.h
/usr/include/KF5/KNewStuff3/knscore/downloadmanager.h
/usr/include/KF5/KNewStuff3/knscore/engine.h
/usr/include/KF5/KNewStuff3/knscore/entryinternal.h
/usr/include/KF5/KNewStuff3/knscore/errorcode.h
/usr/include/KF5/KNewStuff3/knscore/installation.h
/usr/include/KF5/KNewStuff3/knscore/itemsmodel.h
/usr/include/KF5/KNewStuff3/knscore/knewstuffcore_export.h
/usr/include/KF5/KNewStuff3/knscore/provider.h
/usr/include/KF5/KNewStuff3/knscore/question.h
/usr/include/KF5/KNewStuff3/knscore/questionlistener.h
/usr/include/KF5/KNewStuff3/knscore/questionmanager.h
/usr/include/KF5/KNewStuff3/knscore/security.h
/usr/include/KF5/KNewStuff3/knscore/tagsfilterchecker.h
/usr/include/KF5/KNewStuff3/knscore/xmlloader.h
/usr/include/KF5/knewstuff_version.h
/usr/include/KF5/knewstuffcore_version.h
/usr/include/KF5/knewstuffquick_version.h
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
/usr/lib64/qt5/mkspecs/modules/qt_KNewStuff.pri
/usr/lib64/qt5/mkspecs/modules/qt_KNewStuffCore.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5NewStuff.so.5
/usr/lib64/libKF5NewStuff.so.5.57.0
/usr/lib64/libKF5NewStuffCore.so.5
/usr/lib64/libKF5NewStuffCore.so.5.57.0
/usr/lib64/qt5/qml/org/kde/newstuff/libnewstuffqmlplugin.so
/usr/lib64/qt5/qml/org/kde/newstuff/qml/NewStuffItem.qml
/usr/lib64/qt5/qml/org/kde/newstuff/qml/NewStuffList.qml
/usr/lib64/qt5/qml/org/kde/newstuff/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/knewstuff/COPYING.LIB

%files locales -f knewstuff5.lang
%defattr(-,root,root,-)

