%define git 20130112
Name: libclc
Version: 0.0.1
%if 0%git
Release: 0.%git.1
Source0: %name-%git.tar.xz
%else
Release: 1
Source0: %name-%version.tar.xz
%endif
Summary: Implementation of the library of the OpenCL C programming language
Group: Development/Other
License: MIT
URL: http://libclc.llvm.org/
Patch0: 0001-Better-FHS-compliance.patch
Patch1: 0002-Support-for-overriding-generic-implementations.patch
Patch2: 0003-Add-r600-support.patch
BuildRequires: llvm >= 3.2-2 clang >= 3.2-2 python
BuildRequires: llvm-devel >= 3.2-2
BuildArch: noarch

%description
libclc is an open source, BSD/MIT dual licensed implementation of the library
requirements of the OpenCL C programming language, as specified by the
OpenCL 1.1 Specification.
The following sections of the specification impose library requirements:

    6.1: Supported Data Types
    6.2.3: Explicit Conversions
    6.2.4.2: Reinterpreting Types Using as_type() and as_typen()
    6.9: Preprocessor Directives and Macros
    6.11: Built-in Functions
    9.3: Double Precision Floating-Point
    9.4: 64-bit Atomics
    9.5: Writing to 3D image memory objects
    9.6: Half Precision Floating-Point 

libclc is intended to be used with the Clang compiler's OpenCL frontend.

libclc is designed to be portable and extensible. To this end, it provides
generic implementations of most library requirements, allowing the target
to override the generic implementation at the granularity of individual
functions.

%prep
%setup -q -n %name
%apply_patches
python configure.py --prefix=%_prefix --pkgconfigdir=%_datadir/pkgconfig

%build
%make

%install
%makeinstall_std

%files
%_includedir/clc
%_prefix/lib/clc
%_datadir/pkgconfig/*
