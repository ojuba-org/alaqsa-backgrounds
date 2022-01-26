Name: alaqsa-backgrounds
Version: 1.0
Release: 4%{?dist}
Summary: Alaqsa backgrounds
Summary(ar): خلفيات للأقصى
License: WAQFv2
URL: https://ojuba.org
Source0: waqf2-ar.pdf
Source1: ALAQSA_1.JPG
Source2: ALAQSA_2.JPG
Source3: ALAQSA_3.JPG
Source4: ALAQSA_4.JPG

Source100: alaqsa.xml

BuildArch: noarch

%description
Alaqsa backgrounds

%description -l ar
خلفيات للأقصى

%prep
cp %{SOURCE0} .

%install
mkdir -p %{buildroot}%{_datadir}/backgrounds/ALAQSA
mkdir -p %{buildroot}%{_datadir}/gnome-background-properties
install -Dp -m 0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{buildroot}%{_datadir}/backgrounds/ALAQSA
install -Dp -m 0644 %{SOURCE100} %{buildroot}%{_datadir}/gnome-background-properties
%files
%license waqf2-ar.pdf
%{_datadir}/backgrounds/ALAQSA/*
%{_datadir}/gnome-background-properties/alaqsa.xml

%changelog

* Wed Jan 26 2022 Mosaab Alzoubi <moceap@hotmail.com> - 1.0-4
- Rebuilt for F35

* Fri Sep 18 2020 Mosaab Alzoubi <moceap@hotmail.com> - 1.0-3
- Rebuilt for F32

* Tue Feb 21 2017 Mosaab Alzoubi <moceap@hotmail.com> - 1.0-1
- Initial
