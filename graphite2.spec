%define major	2
%define libname %mklibname graphite2_ %{major}
%define devname %mklibname -d graphite2

Summary:	Font rendering capabilities for complex non-Roman writing systems
Name:		graphite2
Version:	1.1.3
Release:	3
Group:		System/Libraries
License:	LGPLv2+
Url:		http://sourceforge.net/projects/silgraphite/
Source0:	http://downloads.sourceforge.net/silgraphite/%{name}-%{version}.tgz
BuildRequires:	cmake
BuildConflicts:	dblatex
BuildRequires:	pkgconfig(freetype2)

%description
Graphite2 is a project within SIL's Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create "smart fonts" 
capable of displaying writing systems with various complex behaviors. With
respect to the Text Encoding Model, Graphite handles the "Rendering" aspect
of writing system implementation.

%package -n	%{libname}
Summary:	Shared libraries for graphite2
Group:		System/Libraries

%description -n	%{libname}
Graphite2 is a project within SIL’s Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create "smart fonts" 
capable of displaying writing systems with various complex behaviors. With
respect to the Text Encoding Model, Graphite handles the "Rendering" aspect
of writing system implementation.

%package -n	%{devname}
Summary:	Development header files and libraries for graphite2
Group:		Development/C++
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	%{_lib}graphite2_2 < 1.1.3-3

%description -n	%{devname}
Includes and definitions for developing with graphite2.

%prep

%setup -q

%build
%cmake -DENABLE_COMPARE_RENDERER=OFF
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libgraphite2.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%{_bindir}/gr2fonttest
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.cmake
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

