%define version 0.9.2
%define release 1

Summary:	A free Japanese dictionary and study assistant
Name:		tagainijisho
Version:	%{version}
Release:	%{release}
Source0:	https://github.com/downloads/Gnurou/tagainijisho/%{name}-%{version}.tar.gz
License:	GPLv3+
Group:	Education		
Url:		http://www.tagaini.net
BuildRequires:	cmake
BuildRequires:	qt4-devel

%description
Tagaini Jisho is a free, open-source Japanese dictionary and kanji lookup tool
that is available for Windows, MacOS X and Linux and aims at becoming your Japanese study assistant. 
It allows you to quickly search for entries and mark those that you wish to study, along with tags and personal notes.
It also let you train entries you are studying and follows your progression in remembering them.
Finally, it makes it easy to review entries you did not remember by listing them on screen or printing them on a small bookle

%prep
%setup -q

%build
%cmake
%make

%install
cd build/
%makeinstall_std

%files
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
