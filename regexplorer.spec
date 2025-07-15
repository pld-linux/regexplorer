Summary:	RegExplorer is a visual regular expression explorer
Summary(pl.UTF-8):	Graficzna przeglądarka wyrażeń regularnych
Name:		regexplorer
Version:	0.1.6
Release:	2
License:	QPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/regexplorer/%{name}-%{version}.tar.bz2
# Source0-md5:	c617505a925c2a2fe5d5bc8cb0f70cb3
Patch0:		%{name}-debian.patch
URL:		http://regexplorer.sourceforge.net/
BuildRequires:	qt-devel
BuildRequires:	tmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RegExplorer is a visual regular expression explorer, it allows for
writing regular expressions and visually see the matches, thus making
regular expression much easier to write and maintain.

%description -l pl.UTF-8
RegExplorer jest graficzną przeglądarką wyrażeń regularnych,
pozwalającą na pisywanie wyrażeń regularnych i graficzny podgląd
dopasowań, przez co wyrażenia regularne są łatwiejsze do zapisywania i
zarządzania.

%prep
%setup -q
%patch -P0 -p1

%build
tmake regexplorer.pro -o Makefile
%{__make} \
	CXXFLAGS="%{rpmcflags} -pipe -Wall -W -DNO_DEBUG" \
	LIBS="%{rpmldflags} -L%{_prefix}/X11R6/%{_lib} -lqt-mt -lXext -lX11 -lm" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D debian/%{name}.1x $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
