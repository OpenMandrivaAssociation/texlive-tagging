# revision 23761
# category Package
# catalog-ctan /macros/latex/contrib/tagging
# catalog-date 2011-08-29 00:41:24 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-tagging
Version:	20110829
Release:	4
Summary:	Document configuration with tags
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tagging
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tagging.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tagging.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to generate multiple documents from
a single source, by marking pieces of the document with tags
and specifying which marked pieces to include or exclude.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tagging/tagging.sty
%doc %{_texmfdistdir}/doc/latex/tagging/README
%doc %{_texmfdistdir}/doc/latex/tagging/tagging.pdf
%doc %{_texmfdistdir}/doc/latex/tagging/tagging.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110829-2
+ Revision: 756507
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110829-1
+ Revision: 719651
- texlive-tagging
- texlive-tagging
- texlive-tagging

