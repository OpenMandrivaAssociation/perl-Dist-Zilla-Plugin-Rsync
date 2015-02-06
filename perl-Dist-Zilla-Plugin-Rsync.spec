%define upstream_name    Dist-Zilla-Plugin-Rsync
%define upstream_version 0.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Dist::Zilla plugin to upload using rsync
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CLASS)
BuildRequires:	perl(Dist::Zilla::Role::Releaser)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
The 'where' config key is required. The 'options' default to '-e ssh'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

