# revision 31491
# category Package
# catalog-ctan /graphics/pgf/contrib/timing-diagrams
# catalog-date 2013-08-21 17:26:35 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-timing-diagrams
Version:	20180303
Release:	1
Summary:	Draw timing diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/timing-diagrams
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/timing-diagrams.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/timing-diagrams.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to draw and annotate various
kinds of timing diagrams, using Tikz. Documentation is sparse,
but the source and the examples file should be of some use.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/timing-diagrams/timing-diagrams.sty
%doc %{_texmfdistdir}/doc/latex/timing-diagrams/Makefile
%doc %{_texmfdistdir}/doc/latex/timing-diagrams/README
%doc %{_texmfdistdir}/doc/latex/timing-diagrams/diagrams-examples.pdf
%doc %{_texmfdistdir}/doc/latex/timing-diagrams/diagrams-examples.tex
%doc %{_texmfdistdir}/doc/latex/timing-diagrams/version.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
