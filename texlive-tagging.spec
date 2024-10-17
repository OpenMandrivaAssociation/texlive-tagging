Name:		texlive-tagging
Version:	52064
Release:	2
Summary:	Document configuration with tags
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tagging
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tagging.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tagging.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
