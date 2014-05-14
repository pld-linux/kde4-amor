#
%define		_state		stable
%define		orgname		amor
%define		qtver		4.8.0

Summary:	amor
Summary(pl.UTF-8):	amor
Name:		kde4-amor
Version:	4.13.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	378f1bc75e534204c3c6143ec614d8e1
URL:		http://www.kde.org/
BuildRequires:	automoc4 >= 0.9.84
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= 4.11.4
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdetoys-amor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
On-Screen Creature.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	.. \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/amor
%{_desktopdir}/kde4/amor.desktop
%{_datadir}/apps/amor
%{_datadir}/dbus-1/interfaces/org.kde.amor.xml
%{_kdedocdir}/en/amor
%{_iconsdir}/hicolor/*x*/apps/amor.png
%{_mandir}/man6/amor.6*
