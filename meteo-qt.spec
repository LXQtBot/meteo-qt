%define aname meteo_qt

Name:           meteo-qt
Version:        1.7
Release:        %mkrel 1
Group:          Graphical desktop/Other
Summary:        Weather status system tray application
License:        GPLv3
URL:            https://github.com/dglent/meteo-qt
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-qt5-devel
BuildRequires:  qttools5
BuildRequires:  imagemagick
Requires:       python3-qt5
Requires:       python3-sip
Requires:       python3-urllib3
Requires:       python3-lxml
Recommends:     qttranslations5

%description
A Qt system tray application for the weather status
Weather data from: http://openweathermap.org/

%prep
%setup -q

%build
%py3_build

%install
%py3_install
%__mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32}/apps
convert -scale 16x16 meteo_qt/images/meteo-qt.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/meteo-qt.png
convert -scale 32x32 meteo_qt/images/meteo-qt.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/meteo-qt.png

%files
%doc TODO CHANGELOG README.md
%exclude %_defaultdocdir/%{name}/LICENSE
%{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{python3_sitelib}/%{aname}-%{version}-py%python3_version.egg-info
%{python3_sitelib}/%{aname}/
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/meteo-qt.png
%{_datadir}/meteo_qt/translations/
