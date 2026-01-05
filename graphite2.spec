%global optflags %{optflags} -O3
%define major 3
%define libname %mklibname graphite2_ %{major}
%define develname %mklibname -d graphite2

Summary:	Font rendering capabilities for complex non-Roman writing systems
Name:		graphite2
Version:	1.3.14
Release:	3
Group:		System/Libraries
License:	LGPLv2+
URL:		https://graphite.sil.org/
# Also: https://github.com/silnrsi/graphite
Source0:	http://downloads.sourceforge.net/silgraphite/%{name}-%{version}.tgz
Patch0:		https://src.fedoraproject.org/rpms/graphite2/raw/master/f/graphite-arm-nodefaultlibs.patch
Patch1:		https://src.fedoraproject.org/rpms/graphite2/raw/master/f/graphite2-1.2.0-cmakepath.patch
Patch2:		graphite-1.3.14-missing-include.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(freetype2)
#BuildConflicts:	dblatex
# required only if building the docs
#BuildRequires:	asciidoc >= 8.6.5 tetex-latex doxygen

%description
Graphite2 is a project within SIL’s Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create "smart fonts" 
capable of displaying writing systems with various complex behaviors. With
respect to the Text Encoding Model, Graphite handles the "Rendering" aspect
of writing system implementation.

%package -n %{libname}
Summary:	Shared libraries for graphite2
Group:		System/Libraries

%description -n %{libname}
Graphite2 is a project within SIL’s Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create "smart fonts" 
capable of displaying writing systems with various complex behaviors. With
respect to the Text Encoding Model, Graphite handles the "Rendering" aspect
of writing system implementation.

%package -n %{develname}
Summary:	Development header files and libraries for graphite2
Group:		Development/C++
Requires:	%{libname} >= %{version}-%{release}
Provides:	graphite2-devel = %{version}-%{release}

%description -n %{develname}
Includes and definitions for developing with graphite2.

%prep
%autosetup -p1

%build
%cmake -DENABLE_COMPARE_RENDERER=OFF -G Ninja
%ninja_build

#%%check
#ctest <- barfs

%install
%ninja_install -C build

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.cmake
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
