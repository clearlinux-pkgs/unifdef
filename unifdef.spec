#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : unifdef
Version  : 2.11
Release  : 6
URL      : http://dotat.at/prog/unifdef/unifdef-2.11.tar.xz
Source0  : http://dotat.at/prog/unifdef/unifdef-2.11.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: unifdef-bin
Requires: unifdef-doc

%description
unifdef - selectively remove C preprocessor conditionals
Written by Tony Finch <dot@dotat.at> - http://dotat.at/prog/unifdef/

%package bin
Summary: bin components for the unifdef package.
Group: Binaries

%description bin
bin components for the unifdef package.


%package doc
Summary: doc components for the unifdef package.
Group: Documentation

%description doc
doc components for the unifdef package.


%prep
%setup -q -n unifdef-2.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496528409
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1496528409
rm -rf %{buildroot}
%make_install
## make_install_append content
mv %{buildroot}/builddir %{buildroot}/usr
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unifdef
/usr/bin/unifdefall

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
