%define debug_package %{nil}

Name:           ukui-search
Version:        0.4.2
Release:        1
Summary:        Advanced ukui menu
License:        GPL-2.0-or-later and GPL-3.0-or-later and Apache-2.0
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.xz
Patch01:        0001-fix-compile-error-of-ukui-search.patch

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
BuildRequires: ukui-interface 

Requires: libukui-search0 ukui-search-systemdbus

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
Requires: libchinese-segmentation0 ukui-search-systemdbus

%description -n libukui-search0
Libraries for ukui-search

%package -n libukui-search-dev
Summary:  libdevel
License:  LGPLv2+
Requires: lbukui-search0 ibchinese-segmentation0 ukui-search-systemdbus

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
%patch01 -p1

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
%{_bindir}/ukui-search
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/applications/*.desktop
#%{_datadir}/ukui-search/translations/*.qm
%{_datadir}/glib-2.0/schemas/*.xml
%{_includedir}/ukui-search/*.h

%files -n libchinese-segmentation0
%{_libdir}/libchinese-segmentation.so.*
%{_datadir}/ukui-search/res/dict/*.utf8

%files -n libchinese-segmentation-dev
%{_includedir}/chinese-seg/*
%{_libdir}/libchinese-segmentation.so

%files -n libukui-search0
%{_libdir}/libukui-search.so.*

%files -n libukui-search-dev
%{_includedir}/ukui-search/*
%{_libdir}/libukui-search.so


%files -n ukui-search-systemdbus
%{_datadir}/dbus-1/system-services/com.ukui.search.qt.systemdbus.service
%{_sysconfdir}/dbus-1/system.d/com.ukui.search.qt.systemdbus.conf
%{_bindir}/ukui-search-systemdbus


%changelog
* Tue Jun 21 2022 peijiankang <peijiankang@kylinos.cn> - 0.4.2-1
- update version to 0.4.2

* Mon May 23 2022 tanyulong <tanyulong@kylinos.cn> - 0.4.1-11
- Improve the project according to the requirements of compliance improvement

* Mon May 09 2022 pei-jiankang <peijiankang@kylinos.cn> - 0.4.1-10
- add ukui-interface BuildRequires

* Tue Dec 07 2021 tanyulong <tanyulong@kylinos.cn> - 0.4.1-9
- Modified fifo path

* Fri Dec 03 2021 tanyulong <tanyulong@kylinos.cn> - 0.4.1-8
- Update app match.cpp info

* Thu Dec 02 2021 tanyulong <tanyulong@kylinos.cn> - 0.4.1-7
- Update debian/changelog 

* Thu Nov 11  2021 tanyulong <tanyulong@kylinos.cn> - 0.4.1-6
- Update changelog for easy view

* Mon Nov 1  2021 tanyulong <tanyulong@kylinos.cn> - 0.4.1-5
- fix Black list wont't work when block home location

* Mon Nov 1  2021 tanyulong <tanyulong@kylinos.cn> - 0.4.1-4
- fix File name is obscured when it's too long in detail page

* Fri Oct 29 2021 tanyulong <tanyulong@kylinos.cn> - 0.4.1-3
- fix Index crash when meet encrypt doc files

* Wed Oct 27 2021 tanyulong <tanyulong@kylin0s.cn> - 0.4.1-2
- Update changelog

* Mon Oct 25 2021 tanyulong <tanyulong@kylinos.cn> - 0.4.1-1
- Init package for openEuler

