Name:           ukui-search
Version:        3.1
Release:        3
Summary:        a user-wide desktop search feature of UKUI desktop environment
License:        GPL-2.0-or-later and GPL-3.0-or-later and Apache-2.0
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires: pkgconf
BuildRequires: gsettings-qt-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qtchooser
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qttools-devel
BuildRequires: xapian-core-devel
BuildRequires: quazip-qt5-devel  quazip-qt5
BuildRequires: glib2-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: uchardet-devel
BuildRequires: poppler-qt5-devel 
BuildRequires: ukui-interface 
BuildRequires: libqtxdg-devel
BuildRequires: libukcc-devel
BuildRequires: opencv
BuildRequires: tesseract-devel


Requires: libukui-search0 ukui-search-systemdbus quazip-qt5

%description
ukui-search is a user-wide desktop search feature of UKUI desktop environment

%package -n libchinese-segmentation0
Summary:  Libraries for chinese-segmentation
License:  LGPLv2+
Provides: libchinese-segmentation
 
%description -n libchinese-segmentation0
 .This package contains a few runtime libraries needed by
 libsearch.

%package -n libchinese-segmentation-devel
Summary:  Libraries for chinese-segmentation development
Requires: libchinese-segmentation0

%description -n libchinese-segmentation-devel
%{summary}.

%package -n libukui-search0
Summary:  Libraries for ukui-search
Provides: libukui-search
Requires: libchinese-segmentation0 ukui-search-systemdbus

%description -n libukui-search0
%{summary}.

%package -n libukui-search-devel
Summary:  Libraries for  ukui-search(development files).
Requires: libukui-search0 libchinese-segmentation0 ukui-search-systemdbus

%description -n libukui-search-devel
%{summary}.

%package -n ukui-search-systemdbus
Summary:  ukui-search-systemdbus is a systembus interface to modify max_user_watches nums permanent.

%description -n ukui-search-systemdbus
%{summary}.

%prep
%setup -q

%build
mkdir build && cd build
%{qmake_qt5} ..
%{make_build}
cd ..
%install
rm -rf $RPM_BUILD_ROOT 
cd build
%{make_install} INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}/usr/share/ukui-search/translations/
cp -r %{_builddir}/%{name}-%{version}/build/frontend/.qm/*.qm %{buildroot}/usr/share/ukui-search/translations/
cp -r %{_builddir}/%{name}-%{version}/build/libsearch/.qm/*.qm %{buildroot}/usr/share/ukui-search/translations/
cp -r %{_builddir}/%{name}-%{version}/build/search-ukcc-plugin/.qm/*.qm %{buildroot}/usr/share/ukui-search/search-ukcc-plugin/translations/

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_bindir}/ukui-search
%{_bindir}/ukui-search-service
%{_bindir}/ukui-search-app-data-service
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/applications/*.desktop
%{_datadir}/ukui-search/translations/tr.qm
%{_datadir}/ukui-search/translations/bo.qm
%{_datadir}/ukui-search/translations/zh_CN.qm
%{_datadir}/glib-2.0/schemas/*.xml
%{_libdir}/ukui-control-center/*
%{_datadir}/ukui-search/search-ukcc-plugin/translations/*
%{_datadir}/ukui-search/search-ukcc-plugin/image/*

%files -n libchinese-segmentation0
%{_libdir}/libchinese-segmentation.so.*
%{_datadir}/ukui-search/res/dict/*

%files -n libchinese-segmentation-devel
%{_includedir}/chinese-seg/*
%{_libdir}/libchinese-segmentation.so

%files -n libukui-search0
%{_libdir}/libukui-search.so.*
%{_datadir}/ukui-search/translations/libukui-search_zh_CN.qm

%files -n libukui-search-devel
%{_includedir}/ukui-search/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libukui-search.so


%files -n ukui-search-systemdbus
%{_datadir}/dbus-1/system-services/com.ukui.search.qt.systemdbus.service
%{_sysconfdir}/dbus-1/system.d/com.ukui.search.qt.systemdbus.conf
%{_bindir}/ukui-search-systemdbus


%changelog
* Fri Feb 10 2023 peijiankang <peijiankang@kylinos.cn> - 3.1-3
- add build debuginfo and debugsource

* Mon Jan 9 2023 peijiankang <peijiankang@kylinos.cn> - 3.1-2
- add search-ukcc-plugin translation files

* Tue Nov 1 2022 peijiankang <peijiankang@kylinos.cn> - 3.1-1
- update version to 3.1

* Wed Jun 22 2022 peijiankang <peijiankang@kylinos.cn> - 0.4.2-3
- fix install error

* Tue Jun 21 2022 peijiankang <peijiankang@kylinos.cn> - 0.4.2-2
- add translation files

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

