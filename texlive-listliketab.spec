%global tl_name listliketab
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset lists as tables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/listliketab
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listliketab.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listliketab.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listliketab.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The listliketab package helps the user make list-like tabulars, i.e., a
tabular that is indistinguishable from an itemize or enumerate
environment. The advantage of using a tabular is that the user can add
additional columns to each entry in the list.

