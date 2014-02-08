# revision 27321
# category TLCore
# catalog-ctan undef
# catalog-date 2012-06-27 22:19:02 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-texdoc
Version:	20120627
Release:	2
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
%{_texmfdistdir}/scripts/tetex/texdoctk.pl
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
%{_texmfdistdir}/texdoc/texdoc.cnf
%{_texmfdistdir}/texdoctk/texdocrc-win32.defaults
%{_texmfdistdir}/texdoctk/texdocrc.defaults
%{_texmfdistdir}/texdoctk/texdoctk.dat
%doc %{_texmfdistdir}/doc/texdoc/News
%doc %{_texmfdistdir}/doc/texdoc/texdoc.pdf
%doc %{_texmfdistdir}/doc/texdoc/texdoc.tex
%doc %{_mandir}/man1/texdoc.1*
%doc %{_texmfdir}/doc/man/man1/texdoc.man1.pdf
%doc %{_mandir}/man1/texdoctk.1*
%doc %{_texmfdir}/doc/man/man1/texdoctk.man1.pdf

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
    ln -sf %{_texmfdistdir}/scripts/tetex/texdoctk.pl texdoctk
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120627-1
+ Revision: 812896
- Update to latest release.

* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091110-4
+ Revision: 759067
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091110-3
+ Revision: 756617
- Rebuild to reduce used resources

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091110-2
+ Revision: 743342
- texlive-texdoc

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091110-1
+ Revision: 719682
- texlive-texdoc
- texlive-texdoc
- texlive-texdoc

