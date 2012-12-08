%define major 2
%define libname %mklibname graphite2_ %{major}
%define develname %mklibname -d graphite2

Summary:	Font rendering capabilities for complex non-Roman writing systems
Name:		graphite2
Version:	1.1.3
Release:	2
Group:		System/Libraries
License:	LGPLv2+
URL:		http://sourceforge.net/projects/silgraphite/
Source0:	http://downloads.sourceforge.net/silgraphite/graphite2-%{version}.tgz
BuildRequires:	cmake
BuildRequires:	pkgconfig(freetype2)
BuildConflicts:	dblatex
# required only if building the docs
#BuildRequires:	asciidoc >= 8.6.5 tetex-latex doxygen

%description
Graphite2 is a project within SIL’s Non-Roman Script Initiative and Language
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

%package -n	%{develname}
Summary:	Development header files and libraries for graphite2
Group:		Development/C++
Requires:	%{libname} >= %{version}-%{release}
Provides:	graphite2-devel = %{version}-%{release}

%description -n	%{develname}
Includes and definitions for developing with graphite2.

%prep

%setup -q

%build
%cmake -DENABLE_COMPARE_RENDERER=OFF
%make
#make docs

#%%check
#ctest <- barfs

%install
%makeinstall_std -C build

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%{_bindir}/*
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc ChangeLog
#%%doc build/doc/manual.html
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.cmake
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Jun 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-1mdv2012.0
+ Revision: 802286
- 1.1.3

* Wed Apr 25 2012 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-1
+ Revision: 793390
- 1.1.2

* Fri Mar 02 2012 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1
+ Revision: 781736
- 1.1.1

* Wed Feb 08 2012 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1
+ Revision: 771850
- 1.1.0
- add backport/update macros

* Wed Sep 28 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-1
+ Revision: 701800
- 1.0.3

* Sun Sep 18 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1
+ Revision: 700222
- fix docs later sometime...
- added a convenient virtual provides (graphite2-devel)
- import graphite2


* Sun Sep 18 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdv2010.2
- initial Mandriva package (fedora import)
