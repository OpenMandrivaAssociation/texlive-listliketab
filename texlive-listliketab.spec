# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/listliketab
# catalog-date 2006-12-08 20:57:43 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-listliketab
Version:	20061208
Release:	1
Summary:	Typeset lists as tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/listliketab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listliketab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listliketab.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listliketab.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The listliketab package helps the user make list-like tabulars,
i.e., a tabular that is indistinguishable from an itemize or
enumerate environment. The advantage of using a tabular is that
the user can add additional columns to each entry in the list.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/listliketab/listliketab.sty
%doc %{_texmfdistdir}/doc/latex/listliketab/README
%doc %{_texmfdistdir}/doc/latex/listliketab/listliketab.pdf
#- source
%doc %{_texmfdistdir}/source/latex/listliketab/listliketab.dtx
%doc %{_texmfdistdir}/source/latex/listliketab/listliketab.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
