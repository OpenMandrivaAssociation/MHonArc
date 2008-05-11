%define name MHonArc
%define version 2.6.16
%define release %mkrel 3

Summary:	A Perl mail-to-HTML converter
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Networking/WWW
URL:		http://www.mhonarc.org/
Source:		http://www.mhonarc.org/release/MHonArc/tar/%{name}-%{version}.tar.bz2
Patch0:         MHonArc-2.6.15-fix-perl.patch 
Requires:	perl >= 0:5.601
BuildRoot:	%{_tmppath}/%{name}%{version}

%description
MHonArc provides HTML mail archiving with index, mail thread linking, etc; plus
other capabilities including support for MIME and powerful user customization
features. 

%prep

%setup -q 
%patch0 -p0

%build

%install
rm -rf %{buildroot}

perl install.me -batch -libpath %{buildroot}%{_libdir}/MHonArc -nodoc \
	-manpath %{buildroot}%{_mandir} -binpath %{buildroot}%{_bindir}

# just in case
cd %{buildroot}
find . -type f -exec perl -pi -e "s|%{buildroot}||g" {} \;

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ACKNOWLG BUGS CHANGES README.txt RELNOTES
%doc doc examples extras logo
%{_bindir}/*
%{_libdir}/MHonArc
%{_mandir}/*/*
