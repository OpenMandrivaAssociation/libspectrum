%define major	8
%define libname	%mklibname spectrum %{major}
%define devname	%mklibname spectrum -d

Summary:	Library to work with ZX Spectrum emulator files
Name:		libspectrum
Version:	1.1.1
Release:	1
Group:		System/Libraries
License:	GPLv2+
Url:		http://fuse-emulator.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz
BuildRequires:	bzip2-devel
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(zlib)

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

%package -n %{libname}
Summary:	Library to work with ZX Spectrum emulator files
Group:		System/Libraries

%description -n %{libname}
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

%package -n %{devname}
Summary:	Development files for programs which will use the libspectrum library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the necessary development libraries and include
files to allow you to develop with libspectrum.

%prep
%setup -q

%build
autoreconf
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libspectrum.so.%{major}*

%files -n %{devname}
%doc COPYING README doc/libspectrum.txt
%{_libdir}/libspectrum.so
%{_includedir}/%{name}.h
%{_mandir}/man3/%{name}.3*

