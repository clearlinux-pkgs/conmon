#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : conmon
Version  : 2.0.32
Release  : 6
URL      : https://github.com/containers/conmon/archive/v2.0.32/conmon-2.0.32.tar.gz
Source0  : https://github.com/containers/conmon/archive/v2.0.32/conmon-2.0.32.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause MIT
Requires: conmon-libexec = %{version}-%{release}
Requires: conmon-license = %{version}-%{release}
BuildRequires : buildreq-golang
BuildRequires : buildreq-meson
BuildRequires : glib-dev
BuildRequires : libseccomp-dev
BuildRequires : pkgconfig(glib-2.0)
Patch1: 0001-Make-libdl-optional-in-meson-definition.patch

%description
[![Total alerts](https://img.shields.io/lgtm/alerts/g/containers/conmon.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/containers/conmon/alerts/)

%package libexec
Summary: libexec components for the conmon package.
Group: Default
Requires: conmon-license = %{version}-%{release}

%description libexec
libexec components for the conmon package.


%package license
Summary: license components for the conmon package.
Group: Default

%description license
license components for the conmon package.


%prep
%setup -q -n conmon-2.0.32
cd %{_builddir}/conmon-2.0.32
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643304546
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/conmon
cp %{_builddir}/conmon-2.0.32/LICENSE %{buildroot}/usr/share/package-licenses/conmon/147d5d72b02467b04653ff37be85b8e201e9af66
cp %{_builddir}/conmon-2.0.32/tools/vendor/github.com/cpuguy83/go-md2man/LICENSE.md %{buildroot}/usr/share/package-licenses/conmon/b7a606730713ac061594edab33cf941704b4a95c
cp %{_builddir}/conmon-2.0.32/tools/vendor/github.com/russross/blackfriday/LICENSE.txt %{buildroot}/usr/share/package-licenses/conmon/da34754c05d40ff81f91de8c1b85ea6e5503e21d
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files libexec
%defattr(-,root,root,-)
/usr/libexec/podman/conmon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/conmon/147d5d72b02467b04653ff37be85b8e201e9af66
/usr/share/package-licenses/conmon/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/conmon/da34754c05d40ff81f91de8c1b85ea6e5503e21d
