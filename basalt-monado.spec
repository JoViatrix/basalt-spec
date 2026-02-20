%global commit 864d267
%global datetimever 202602200242864d267

Name: basalt-monado
Version: 202602200242864d267
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

%{_libdir}/libbasalt.so*
%{_libdir}/pkgconfig/basalt.pc


%changelog
* Fri Feb 20 2026 GitHub Actions <actions@github.com> - 202602200242864d267-1
- Auto-update to Basalt commit 864d267

* Thu Feb 19 2026 GitHub Actions <actions@github.com> - 20260219024790cdaec-1
- Auto-update to Basalt commit 90cdaec

* Fri Feb 06 2026 GitHub Actions <actions@github.com> - 202602060242d0953ee-1
- Auto-update to Basalt commit d0953ee

* Thu Jan 29 2026 GitHub Actions <actions@github.com> - 202601290238e4e81cb-1
- Auto-update to Basalt commit e4e81cb

* Tue Jan 06 2026 GitHub Actions <actions@github.com> - 2026010602110ff2da4-1
- Auto-update to Basalt commit 0ff2da4

* Mon Jan 05 2026 GitHub Actions <actions@github.com> - 2026010502282049d90-1
- Auto-update to Basalt commit 2049d90

* Sat Dec 20 2025 GitHub Actions <actions@github.com> - 202512200201df56acf-1
- Auto-update to Basalt commit df56acf

* Thu Dec 18 2025 GitHub Actions <actions@github.com> - 2025121802042d23473-1
- Auto-update to Basalt commit 2d23473

* Wed Dec 10 2025 GitHub Actions <actions@github.com> - 2025121002079c37523-1
- Auto-update to Basalt commit 9c37523

* Tue Oct 5 2025 Manual Actions
- update lib paths

* Tue Sep 30 2025 GitHub Actions <actions@github.com> - 2025093001505337898-1
- Auto-update to Basalt commit 5337898

* Sat Sep 13 2025 GitHub Actions <actions@github.com> - 2025091301443388c6e-1
- Auto-update to Basalt commit 3388c6e

* Wed Jul 23 2025 GitHub Actions <actions@github.com> - 202507230220dc6ef9f-1
- Auto-update to Basalt commit dc6ef9f

* Fri Jul 18 2025 GitHub Actions <actions@github.com> - 2025071810218a45e15-1
- Auto-update to Basalt commit 8a45e15


%autochangelog

