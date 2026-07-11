%global tl_name texdoc
%global tl_revision 73876

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.1.1
Release:	%{tl_revision}.1
Summary:	Documentation access for TeX Live
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texdoc
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdoc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(kpathsea)
Requires:	texlive(texdoc.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
texdoc is a Lua script providing easy access to the documentation in TeX
Live: PDF, DVI, plain text files, and more. Viewing and other
configuration can be extensively customized. It is distributed with TeX
Live; MiKTeX provides a program by the same name to do the same job, but
its implementation is unrelated.

