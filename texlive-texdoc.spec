# revision 24354
# category TLCore
# catalog-ctan undef
# catalog-date 2009-11-10 00:58:07 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-texdoc
Version:	20091110
Release:	1
Summary:	Documentation access for TeX distributions
Group:		Publishing
URL:		http://tug.org/texlive
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdoc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-texdoc.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXdoc is an application for easy access to the package
documentation of a TeX distributions (i.e., .dvi, .pdf or .ps
files on the $TEXDOCS tree). It is distributed with TeX-Live
and a derivative is distributed with miktex.

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
%{_bindir}/texdoc
%{_bindir}/texdoctk
%{_texmfdistdir}/texdoc/texdoc.cnf
%{_texmfdir}/scripts/tetex/texdoctk.pl
%{_texmfdir}/scripts/texdoc/Data.meta.lua
%{_texmfdir}/scripts/texdoc/Data.tlpdb.lua
%{_texmfdir}/scripts/texdoc/alias.tlu
%{_texmfdir}/scripts/texdoc/config.tlu
%{_texmfdir}/scripts/texdoc/constants.tlu
%{_texmfdir}/scripts/texdoc/functions.tlu
%{_texmfdir}/scripts/texdoc/main.tlu
%{_texmfdir}/scripts/texdoc/score.tlu
%{_texmfdir}/scripts/texdoc/search.tlu
%{_texmfdir}/scripts/texdoc/texdoc.tlu
%{_texmfdir}/scripts/texdoc/texdoclib.tlu
%{_texmfdir}/scripts/texdoc/view.tlu
%{_texmfdir}/texdoctk/texdocrc-win32.defaults
%{_texmfdir}/texdoctk/texdocrc.defaults
%{_texmfdir}/texdoctk/texdoctk.dat
%doc %{_mandir}/man1/texdoc.1*
%doc %{_texmfdir}/doc/man/man1/texdoc.man1.pdf
%doc %{_mandir}/man1/texdoctk.1*
%doc %{_texmfdir}/doc/man/man1/texdoctk.man1.pdf
%doc %{_texmfdir}/doc/texdoc/News
%doc %{_texmfdir}/doc/texdoc/texdoc.pdf
%doc %{_texmfdir}/doc/texdoc/texdoc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

perl -pi -e 's%^# (viewer_pdf = )xpdf.*%$1xdg-open%;'	\
	texmf-dist/texdoc/texdoc.cnf

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdir}/scripts/texdoc/texdoc.tlu texdoc
    ln -sf %{_texmfdir}/scripts/tetex/texdoctk.pl texdoctk
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
