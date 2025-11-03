Name:		hyprlauncher
Version:	0.1.3
Release:	1
Source0:	https://github.com/hyprwm/hyprlauncher/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:	A multipurpose and versatile launcher / picker for Hyprland
URL:		https://github.com/hyprlauncher/hyprlauncher
License:	BSD-3-Clause
Group:		Window Manager/Hyprland

BuildSystem:	cmake

BuildRequires:	pkgconfig(hyprtoolkit)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprwire)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:	hyprwire
BuildRequires:	pkgconfig(aquamarine)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(xkbcommon)

Requires:	wl-clipboard

%description
A multipurpose and versatile launcher / picker for Hyprland

%prep
%autosetup -p1

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
