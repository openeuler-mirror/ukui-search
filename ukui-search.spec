%define debug_package %{nil}

Name:           ukui-search
Version:        0.4.1
Release:        3
Summary:        Advanced ukui menu
License:        GPL-3.0
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

Patch0:        0001-Update-changelog.patch
Patch1:        0002-fix-Index-crash-when-meet-encrypt-doc-files.patch

BuildRequires: pkgconf
BuildRequires: gsettings-qt-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qtchooser
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qttools-devel
BuildRequires: xapian-core-devel
BuildRequires: quazip-qt5-devel  
BuildRequires: glib2-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: uchardet-devel
BuildRequires: poppler-qt5-devel 




%description
 Portable, efficient middle-ware for different kinds of mail access


%package -n libchinese-segmentation0
Summary:  libs
License:  LGPLv2+
Provides: libchinese-segmentation
 
%description -n libchinese-segmentation0
 Libraries for chinese-segmentation
 .This package contains a few runtime libraries needed by
 libsearch.



%package -n libchinese-segmentation-dev
Summary:  libs
License:  LGPLv2+
Provides: libchinese-segmentation

%description -n libchinese-segmentation-dev
 Libraries for chinese-segmentation
 .This package contains a few runtime libraries needed by
 libsearch.


%package -n libukui-search0
Summary:  libs
License:  LGPLv2+
Provides: libukui-search

%description -n libukui-search0
Libraries for ukui-search



%package -n libukui-search-dev
Summary:  libdevel
License:  LGPLv2+

%description -n libukui-search-dev
Libraries for  ukui-search(development files).



%package -n ukui-search-systemdbus
Summary:  libdevel
License:  LGPLv2+

%description -n ukui-search-systemdbus
ukui-search-systemdbus is a systembus interface to modify max_user_watches nums 
permanent.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
mkdir build && cd build
qmake-qt5 ..
make

%install
rm -rf $RPM_BUILD_ROOT 
cd %{_builddir}/%{name}-%{version}/build
make INSTALL_ROOT=%{buildroot} install

%clean
rm -rf $RPM_BUILD_ROOT

%files 
/usr/share/applications/ukui-search-menu.desktop
/etc/xdg/autostart/ukui-search.desktop
/usr/bin/ukui-search
/usr/include/ukui-search/*.h
/usr/share/glib-2.0/schemas/org.ukui.log4qt.ukui-search.gschema.xml
/usr/share/glib-2.0/schemas/org.ukui.search.data.gschema.xml

%files -n libchinese-segmentation0
/usr/lib64/libchinese-segmentation.so.*
/usr/share/ukui-search/res/dict/*.utf8

%files -n libchinese-segmentation-dev
/usr/include/chinese-seg/*
/usr/lib64/libchinese-segmentation.so


%files -n libukui-search0
/usr/lib64/libukui-search.so.*


%files -n libukui-search-dev
/usr/include/ukui-search/*
/usr/lib64/libukui-search.so


%files -n ukui-search-systemdbus
/usr/share/dbus-1/system-services/com.ukui.search.qt.systemdbus.service
/etc/dbus-1/system.d/com.ukui.search.qt.systemdbus.conf
/usr/bin/ukui-search-systemdbus






%changelog
* Fri Oct 29 2021 tanyulong <tanyulong@kylinos.cn> - 0.4.1-3
- fix Index crash when meet encrypt doc files

* Wed Oct 27 2021 tanyulong <tanyulong@kylin0s.cn> - 0.4.1-2
-  Update changelog

* Mon Oct 25 2021 tanyulong <tanyulong@kylinos.cn> - 0.4.1-1
- Init package for openEuler

