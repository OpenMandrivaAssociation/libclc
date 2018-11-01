%define git	20181101
# create archive
# git clone http://llvm.org/git/libclc.git
# export PKG=libclc-$(date +%Y%m%d)
# git archive --prefix $PKG/ --format tar HEAD | xz > $PKG.tar.xz

Summary:	Implementation of the library of the OpenCL C programming language
Name:		libclc
Version:	0.0.1
%if 0%{git}
Release:	0.%{git}.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	2
Source0:	%{name}-%{version}.tar.xz
%endif
Source1:	%{name}.rpmlintrc
Group:		Development/Other
License:	MIT
Url:		http://libclc.llvm.org/
BuildArch:	noarch
BuildRequires:	clang >= 3.3
BuildRequires:	llvm >= 3.3
BuildRequires:	python2
BuildRequires:	llvm-devel >= 3.3

%description
libclc is an open source, BSD/MIT dual licensed implementation of the library
requirements of the OpenCL C programming language, as specified by the
OpenCL 1.1 Specification.
The following sections of the specification impose library requirements:

    6.1:	Supported Data Types
    6.2.3:	Explicit Conversions
    6.2.4.2:	Reinterpreting Types Using as_type() and as_typen()
    6.9:	Preprocessor Directives and Macros
    6.11:	Built-in Functions
    9.3:	Double Precision Floating-Point
    9.4:	64-bit Atomics
    9.5:	Writing to 3D image memory objects
    9.6:	Half Precision Floating-Point 

libclc is intended to be used with the Clang compiler's OpenCL frontend.

libclc is designed to be portable and extensible. To this end, it provides
generic implementations of most library requirements, allowing the target
to override the generic implementation at the granularity of individual
functions.

%prep
%setup -qn %{name}-%{git}
%apply_patches

python2 configure.py \
	--prefix=%{_prefix} \
	--pkgconfigdir=%{_datadir}/pkgconfig

sed -i -e "s,/generic,`pwd`/generic,g" Makefile
# fstack-protector-strong is currently not supported by clang++
sed -i "s/fstack-protector-strong/fstack-protector/" Makefile

%build
%make

%install
%makeinstall_std

%files
%{_includedir}/clc
%{_prefix}/lib/clc
%{_datadir}/pkgconfig/*
