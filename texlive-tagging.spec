%global tl_name tagging
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.0.1
Release:	%{tl_revision}.1
Summary:	Document configuration with tags
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tagging
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tagging.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tagging.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the user to generate multiple documents from a single
source, by marking pieces of the document with tags and specifying which
marked pieces to include or exclude.

