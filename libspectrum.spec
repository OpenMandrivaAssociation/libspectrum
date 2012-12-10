%define lib_major	8
%define lib_name	%mklibname spectrum %{lib_major}
%define devel_name	%mklibname spectrum -d
%define old_lib_name	%mklibname spectrum 7
%define older_lib_name	%mklibname spectrum 5
%define oldest_lib_name	%mklibname spectrum 2
%define old_devel_name	%mklibname spectrum 2 -d

Name:		libspectrum
Version: 	1.0.0
Release:	3

Summary:	Library to make the input and output of ZX Spectrum emulator files easier
License:	GPLv2+
Group:		System/Libraries
URL:		http://fuse-emulator.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz

BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	perl
BuildRequires:	autoconf

%description
libspectrum is a fairly simple library designed to make the handling
of various ZX Spectrum emulator-related file formats easy.  So far it
handles:

* Snapshots: .z80, .szx, .sna (all read/write), .zxs, .sp., .snp and
  +D snapshots (read only).
* Tape images: .tzx, .tap (read/write) and Warajevo .tap (read only).
* Input recordings: .rzx (read/write).
* Timex cartridges: .dck (read only).
* IDE hard disk images: .hdf (read/write).

%package -n %{lib_name}
Summary:	A library to make the input and output of ZX Spectrum emulator files easier
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{old_lib_name} < %{version}-%{release}
Obsoletes:	%{older_lib_name} < %{version}-%{release}
Obsoletes:	%{oldest_lib_name} < %{version}-%{release}

%description -n %{lib_name}
libspectrum is a library which is designed to make the input and
output of ZX Spectrum emulator files slightly easier than it would be
otherwise. It should hopefully compile and run on Unix-based systems,
Win32 and Mac OS X.

Currently supported are:

* Snapshots: .z80, .szx, .sna (all read/write), .zxs, .sp., .snp and
  +D snapshots (read only).
* Tape images: .tzx, .tap (read/write) and Warajevo .tap (read only).
* Input recordings: .rzx (read/write).
* Timex cartridges: .dck (read only).
* IDE hard disk images: .hdf (read/write).

This package provides the libraries to handle ZX Spectrum emulator files.

%package -n %{devel_name}
Summary:	Development files for programs which will use the libspectrum library
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{old_devel_name} < %{version}-%{release}

%description -n %{devel_name}
This package provides the necessary development libraries and include
files to allow you to develop with libspectrum.

%prep
%setup -q

%build
autoreconf
%configure
%make

%install
%makeinstall_std

%files -n %{lib_name}
%doc ChangeLog THANKS COPYING AUTHORS
%{_libdir}/*.so.*

%files -n %{devel_name}
%defattr(0644,root,root,0755)
%doc COPYING README doc/libspectrum.txt
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%{_mandir}/*/*



%changelog
* Tue Jan 17 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0.0-2mdv2012.0
+ Revision: 762004
- Rebuild for .la files issue

* Wed Jul 27 2011 Andrey Bondrov <abondrov@mandriva.org> 1.0.0-1
+ Revision: 691925
- Fix BuildRequires
- New version 1.0.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ending-with-dot

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 20 2007 Olivier Thauvin <nanardon@mandriva.org> 0.3.0.1-1mdv2008.0
+ Revision: 28814
- 0.3.0.1
- Import libspectrum



* Wed Apr 21 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.2.1-1mdk
- 0.2.1

* Mon Dec 15 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.2.0.1-3mdk
- introduce in contrib

* Sat Nov 1 2003 Miguel Barrio Orsikowsky <mik@ingecivil.com> 0.2.0.1-2mdk
- made lots of fixes and cosmetic changes to the spec file

* Thu Sep 2 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.2.0.1-1mdk
- new version

* Sun Jul 27 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.1.1-4mdk
- fixed crashes when loading certain snapshots into +2A and +3
- fixed a small thinko in the RZX code which could cause segfaults

* Thu May 22 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.1.1-3mdk
- added BuildRequires

* Tue May 13 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.1.1-2mdk
- unified %%changelog

* Sun Apr 27 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.1.1-1mdk
- new version

* Thu Apr 24 2003 Miguel Barrio Orsikowsky <megamik@ya.com> 0.1.0-1mdk
- first version of the package
- spec file written using Mandrake RPM HOWTO 1.1.1
