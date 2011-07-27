Name:			libspectrum
Version: 		1.0.0
Release:		%mkrel 1

%define lib_major	8
%define lib_name	%mklibname spectrum %{lib_major}
%define devel_name	%mklibname spectrum -d
%define old_lib_name	%mklibname spectrum 7
%define older_lib_name	%mklibname spectrum 5
%define oldest_lib_name	%mklibname spectrum 2
%define old_devel_name	%mklibname spectrum 2 -d

Summary:	Library to make the input and output of ZX Spectrum emulator files easier
License:	GPLv2+
Group:		System/Libraries
URL:		http://fuse-emulator.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz

BuildRequires:	libz-devel
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	libglib2-devel
BuildRequires:	perl
BuildRequires:	autoconf
BuildRequires:  audiofile-devel >= 0.2.3
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
Obsoletes:	%{old_lib_name}
Obsoletes:	%{older_lib_name}
Obsoletes:	%{oldest_lib_name}

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
Obsoletes:	%{old_devel_name}

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
rm -rf %{buildroot}
%makeinstall

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(0644,root,root,0755)
%_libdir/*.so.*
%doc ChangeLog THANKS COPYING AUTHORS

%files -n %{devel_name}
%defattr(0644,root,root,0755)
%doc COPYING README doc/libspectrum.txt
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*.h
%{_mandir}/*/*

