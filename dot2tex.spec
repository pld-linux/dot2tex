Summary:	A Graphviz to LaTeX converter
Summary(hu.UTF-8):	Egy Graphviz-ből LaTeX-be konvertáló program
Summary(pl.UTF-8):	Konwerter plików Graphviza do LaTeXa
Name:		dot2tex
Version:	2.8.6
Release:	2
License:	MIT
Group:		Applications
Source0:	http://dot2tex.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	8af7c44ea6484d47faee31cacbad9206
URL:		http://www.fauskes.net/code/dot2tex/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
Requires:	graphviz
Requires:	python-pyparsing >= 1.4.8
Requires:	texlive-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dot2tex is a tool for converting graphs rendered by Graphviz to
formats that can be used with LaTeX.

%description -l hu.UTF-8
dot2tex egy eszköz, amellyel a Graphviz által feldolgozandó gráfokat
LaTeX-ben használható formátumokba alakít.

%description -l pl.UTF-8
dot2tex jest narzędziem do konwertowania grafów stworzonych przez
Graphviza do formatów, które mogą być użyte z LaTeXem.

%package doc
Summary:	dot2tex documentation
Summary(hu.UTF-8):	dot2tex dokumentáció
Summary(pl.UTF-8):	Dokumentacja programu dot2tex
Group:		Documentation

%description doc
dot2tex documentation.

%description doc -l hu.UTF-8
dot2tex dokumentáció.

%description doc -l pl.UTF-8
Dokumentacja programu dot2tex.

%package examples
Summary:	Examples for dot2tex
Summary(hu.UTF-8):	Példák dot2tex-hez
Summary(pl.UTF-8):	Przykłady dla dot2tex
Group:		Documentation

%description examples
Examples for dot2tex.

%description examples -l hu.UTF-8
Példák dot2tex-hez.

%description examples -l pl.UTF-8
Przykłady dla dot2tex.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%{__cp} -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt changelog.txt
%attr(755,root,root) %{_bindir}/dot2tex
%dir %{py_sitescriptdir}/dot2tex
%{py_sitescriptdir}/dot2tex/*.py[co]
%{py_sitescriptdir}/dot2tex-*.egg-info

%files doc
%defattr(644,root,root,755)
%doc doc/usage.html doc/img/ doc/docgraphs/

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
