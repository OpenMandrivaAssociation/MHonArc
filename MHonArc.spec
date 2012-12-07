Summary:	A Perl mail-to-HTML converter
Name:		MHonArc
Version:	2.6.18
Release:	6
License:	GPL
Group:		Networking/WWW
URL:		http://www.mhonarc.org/
Source:		http://www.mhonarc.org/release/MHonArc/tar/%{name}-%{version}.tar.gz
Patch0:		MHonArc-2.6.15-fix-perl.patch
Requires:	perl
Provides:	mhonarc = %{version}-%{release}
BuildArch:	noarch

%description
MHonArc provides HTML mail archiving with index, mail thread linking, etc; plus
other capabilities including support for MIME and powerful user customization
features. 

%prep
%setup -q
%patch0 -p1

%build

%install
perl install.me -batch -libpath %{buildroot}%{_datadir}/MHonArc -nodoc \
	-manpath %{buildroot}%{_mandir} -binpath %{buildroot}%{_bindir}

# just in case
cd %{buildroot}
find . -type f -exec perl -pi -e "s|%{buildroot}||g" {} \;

%files
%doc ACKNOWLG BUGS CHANGES README.txt RELNOTES
%doc doc examples extras logo
%{_bindir}/*
%{_datadir}/MHonArc
%{_mandir}/*/*

