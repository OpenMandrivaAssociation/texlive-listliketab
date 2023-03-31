Name:		texlive-listliketab
Version:	15878
Release:	2
Summary:	Typeset lists as tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/listliketab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listliketab.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listliketab.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listliketab.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The listliketab package helps the user make list-like tabulars,
i.e., a tabular that is indistinguishable from an itemize or
enumerate environment. The advantage of using a tabular is that
the user can add additional columns to each entry in the list.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/listliketab/listliketab.sty
%doc %{_texmfdistdir}/doc/latex/listliketab/README
%doc %{_texmfdistdir}/doc/latex/listliketab/listliketab.pdf
#- source
%doc %{_texmfdistdir}/source/latex/listliketab/listliketab.dtx
%doc %{_texmfdistdir}/source/latex/listliketab/listliketab.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
