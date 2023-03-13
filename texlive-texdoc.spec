Name:		texlive-texdoc
Version:	66228
Release:	1
Summary:	Documentation access for TeX distributions
Group:		Publishing
URL:		http://tug.org/texlive
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdoc.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/scripts/texdoc
%{_texmfdistdir}/texdoc
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/support/texdoc

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

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
