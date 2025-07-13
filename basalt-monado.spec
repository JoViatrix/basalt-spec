%global commit main
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: basalt
Version: %{?buildtime}%{?dist}
Release: %autorelease
Summary: Basalt for Monado

License: BSD-3-Clause
URL: https://gitlab.freedesktop.org/mateosss/basalt
# Source0: https://gitlab.freedesktop.org/mateosss/basalt/-/archive/%{commit}/basalt-%{commit}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: mold
BuildRequires: git
BuildRequires: tbb-devel
BuildRequires: glew-devel
BuildRequires: ccache
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: lz4-devel
BuildRequires: bzip2-devel
BuildRequires: boost-devel
BuildRequires: boost-regex
BuildRequires: boost-filesystem
BuildRequires: boost-date-time
BuildRequires: boost-program-options
BuildRequires: gtest-devel
BuildRequires: opencv-devel
BuildRequires: fmt-devel
BuildRequires: pkgconfig(eigen3)
BuildRequires: libepoxy-devel
BuildRequires: libxkbcommon-devel

%description
A fork of Basalt improved for tracking XR devices with Monado.

%prep
%autosetup -n %{name}-%{commit}
git clone --recursive https://gitlab.freedesktop.org/mateosss/basalt.git %{name}-%{commit}

%build
%cmake --preset library
%cmake_build


%install
%cmake_install


%check


%files
%license
%doc

%{_datarootdir}/basalt/*

%{_prefix}/lib/debug/usr/lib/libbasalt.so.*
%{_prefix}/lib/libbasalt.so*
%{_prefix}/lib/pkgconfig/basalt.pc


%changelog
%autochangelog

