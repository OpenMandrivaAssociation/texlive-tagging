# revision 23761
# category Package
# catalog-ctan /macros/latex/contrib/tagging
# catalog-date 2011-08-29 00:41:24 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-tagging
Version:	20110829
Release:	1
Summary:	Document configuration with tags
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tagging
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tagging.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tagging.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package allows the user to generate multiple documents from
a single source, by marking pieces of the document with tags
and specifying which marked pieces to include or exclude.

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
%{_texmfdistdir}/tex/latex/tagging/tagging.sty
%doc %{_texmfdistdir}/doc/latex/tagging/README
%doc %{_texmfdistdir}/doc/latex/tagging/tagging.pdf
%doc %{_texmfdistdir}/doc/latex/tagging/tagging.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
