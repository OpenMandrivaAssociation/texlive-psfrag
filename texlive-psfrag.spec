# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/psfrag
# catalog-date 2009-10-07 22:25:55 +0200
# catalog-license other-free
# catalog-version 3.04
Name:		texlive-psfrag
Version:	3.04
Release:	1
Summary:	Replace strings in encapsulated PostScript figures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/psfrag
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfrag.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfrag.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psfrag.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Allows LaTeX constructions (equations, picture environments,
etc.) to be precisely superimposed over Encapsulated PostScript
figures, using your own favorite drawing tool to create an EPS
figure and placing simple text 'tags' where each replacement is
to be placed, with PSfrag automatically removing these tags
from the figure and replacing them with a user specified LaTeX
construction, properly aligned, scaled, and/or rotated.

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
