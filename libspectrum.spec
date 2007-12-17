%define name    libspectrum
%define version 0.3.0.1
%define release %mkrel 1

%define libname %mklibname spectrum 2
%define libname_devel %mklibname -d spectrum 2
%define libname_static_devel %mklibname -s -d spectrum 2

Name: %{name}
Summary: A library to make the input and output of ZX Spectrum emulator files easier
Version: %{version}
Release: %{release}
License: GPL
URL: http://www.srcf.ucam.org/~pak21/spectrum/libspectrum.html
Source: http://www.srcf.ucam.org/~pak21/spectrum/%{name}-%{version}.tar.gz
Group: System/Libraries
BuildRequires: libz-devel libgcrypt-devel libglib-devel perl

%description
libspectrum is a fairly simple library designed to make the handling
of various ZX Spectrum emulator-related file formats easy.  So far it
handles .sna and .z80 snapshots (.sna read only), .tap and .tzx tape
images and .rzx input recording files.

%package -n %{libname}
Summary: A library to make the input and output of ZX Spectrum emulator files easier
Group: System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
libspectrum is a fairly simple library designed to make the handling
of various ZX Spectrum emulator-related file formats easy.  So far it
handles .sna and .z80 snapshots (.sna read only), .tap and .tzx tape
images and .rzx input recording files.

Using the libspectrum API requires to use the libspectrum library.

%package -n %{libname_devel}
Summary: Development files for programs which will use the libspectrum library
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{libname_devel}
This package contains the header files and documentation necessary for
development of programs that will use the libspectrum library.

You should install this package if you need to develop programs which will
use the libspectrum library functions. You'll also need to install the
libspectrum package.

%package -n %{libname_static_devel}
Summary: Static libraries for programs which will use the libspectrum library
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-static-devel = %{version}-%{release}

%description -n %{libname_static_devel}
This package contains the static libraries, necessary for development of
programs that will use the libspectrum library.

You should install this package if you need to develop programs which will
use the libspectrum library functions. You'll also need to install the
libspectrum package.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog README THANKS COPYING AUTHORS
%{_libdir}/lib*.so.*

%files -n %{libname_devel}
%defattr(-,root,root)
%doc COPYING doc/libspectrum.txt
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_mandir}/man3/*

%files -n %{libname_static_devel}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/lib*.a
