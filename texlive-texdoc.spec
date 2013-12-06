# revision 29764
# category TLCore
# catalog-ctan undef
# catalog-date 2012-06-27 22:19:02 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-texdoc
Version:	20120627
Release:	5
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

%description
TeXdoc is an application for easy access to the package
documentation of a TeX distributions (i.e., .dvi, .pdf or .ps
files on the $TEXDOCS tree). It is distributed with TeX-Live
and a derivative is distributed with miktex.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texdoc
%{_bindir}/texdoctk
%{_texmfdistdir}/scripts/texdoc/Data.meta.lua
%{_texmfdistdir}/scripts/texdoc/Data.tlpdb.lua
%{_texmfdistdir}/scripts/texdoc/alias.tlu
%{_texmfdistdir}/scripts/texdoc/config.tlu
%{_texmfdistdir}/scripts/texdoc/constants.tlu
%{_texmfdistdir}/scripts/texdoc/functions.tlu
%{_texmfdistdir}/scripts/texdoc/main.tlu
%{_texmfdistdir}/scripts/texdoc/score.tlu
%{_texmfdistdir}/scripts/texdoc/search.tlu
%{_texmfdistdir}/scripts/texdoc/texdoc.tlu
%{_texmfdistdir}/scripts/texdoc/texdoclib.tlu
%{_texmfdistdir}/scripts/texdoc/view.tlu
%{_texmfdistdir}/scripts/texdoctk/texdoctk.pl
%{_texmfdistdir}/texdoc/texdoc.cnf
%{_texmfdistdir}/texdoctk/texdocrc-win32.defaults
%{_texmfdistdir}/texdoctk/texdocrc.defaults
%{_texmfdistdir}/texdoctk/texdoctk.dat
%doc %{_mandir}/man1/texdoc.1*
%doc %{_texmfdistdir}/doc/man/man1/texdoc.man1.pdf
%doc %{_mandir}/man1/texdoctk.1*
%doc %{_texmfdistdir}/doc/man/man1/texdoctk.man1.pdf
%doc %{_texmfdistdir}/doc/texdoc/News
%doc %{_texmfdistdir}/doc/texdoc/texdoc.pdf
%doc %{_texmfdistdir}/doc/texdoc/texdoc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

perl -pi -e 's%^# (viewer_pdf = )xpdf.*%$1xdg-open%;'	\
	texmf-dist/texdoc/texdoc.cnf

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/texdoc/texdoc.tlu texdoc
    ln -sf %{_texmfdistdir}/scripts/texdoctk/texdoctk.pl texdoctk
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
