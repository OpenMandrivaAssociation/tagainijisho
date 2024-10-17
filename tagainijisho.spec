Summary:	A free Japanese dictionary and study assistant
Name:		tagainijisho
Version:	1.2.2
Release:	1
Source0:	https://github.com/Gnurou/tagainijisho/archive/refs/tags/%{version}.tar.gz
Source1:	http://ftp.edrdg.org/pub/Nihongo/JMdict.gz
Source2:	https://www.edrdg.org/kanjidic/kanjidic2.xml.gz
Source3:	https://github.com/KanjiVG/kanjivg/releases/download/r20220427/kanjivg-20220427.xml.gz
License:	GPLv3+
Group:		Education		
Url:		https://www.tagaini.net
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5)

%description
Tagaini Jisho is a free, open-source Japanese dictionary and kanji lookup tool
that is available for Windows, MacOS X and Linux and aims at becoming your Japanese study assistant. 
It allows you to quickly search for entries and mark those that you wish to study, along with tags and personal notes.
It also let you train entries you are studying and follows your progression in remembering them.
Finally, it makes it easy to review entries you did not remember by listing them on screen or printing them on a small bookle

%prep
%autosetup -p1
mkdir 3rdparty
gzip -cd %{S:1} >3rdparty/JMdict
gzip -cd %{S:2} >3rdparty/kanjidic2.xml
gzip -cd %{S:3} >3rdparty/kanjivg.xml
%cmake \
	-DEMBED_SQLITE:BOOL=OFF \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/tagainijisho.appdata.xml
