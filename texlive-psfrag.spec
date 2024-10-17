Name:		texlive-psfrag
Version:	15878
Release:	2
Summary:	Replace strings in encapsulated PostScript figures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/psfrag
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfrag.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfrag.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfrag.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%define		_unpackaged_subdirs_terminate_build	0

%description
Allows LaTeX constructions (equations, picture environments,
etc.) to be precisely superimposed over Encapsulated PostScript
figures, using your own favorite drawing tool to create an EPS
figure and placing simple text 'tags' where each replacement is
to be placed, with PSfrag automatically removing these tags
from the figure and replacing them with a user specified LaTeX
construction, properly aligned, scaled, and/or rotated.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/psfrag/psfrag.pro
%{_texmfdistdir}/tex/latex/psfrag/psfrag.sty
%doc %{_texmfdistdir}/doc/latex/psfrag/00readme.txt
%doc %{_texmfdistdir}/doc/latex/psfrag/announce.txt
%doc %{_texmfdistdir}/doc/latex/psfrag/example.eps
%doc %{_texmfdistdir}/doc/latex/psfrag/pfgguide.pdf
%doc %{_texmfdistdir}/doc/latex/psfrag/pfgguide.tex
%doc %{_texmfdistdir}/doc/latex/psfrag/testfig.eps
#- source
%doc %{_texmfdistdir}/source/latex/psfrag/psfrag.dtx
%doc %{_texmfdistdir}/source/latex/psfrag/psfrag.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
