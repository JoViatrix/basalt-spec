%global commit 8a45e15
%global datetimever 2025071810218a45e15

Name: basalt-monado
Version: 2025071810218a45e15
Release: 1%{?dist}
Summary: Basalt for Monado

License: BSD-3-Clause
URL: https://gitlab.freedesktop.org/mateosss/basalt

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
BuildRequires: suitesparse-devel


%description
A fork of Basalt improved for tracking XR devices with Monado.


%prep
git clone --recurse-submodules https://gitlab.freedesktop.org/mateosss/basalt.git %{name}-%{commit}
cd %{name}-%{commit}
git checkout %{commit}
git submodule update --init --recursive


%build
%cmake --preset library %{name}-%{commit}
%cmake_build


%install
%cmake_install


%check


%files
%license
%doc

%{_datarootdir}/basalt/*

%{_prefix}/lib/libbasalt.so*
%{_prefix}/lib/pkgconfig/basalt.pc


%changelog
* Fri Jul 18 2025 GitHub Actions <actions@github.com> - 2025071810218a45e15-1
- Auto-update to Basalt commit 8a45e15


%autochangelog

