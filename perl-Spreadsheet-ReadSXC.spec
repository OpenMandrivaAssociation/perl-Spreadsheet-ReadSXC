%define upstream_name    Spreadsheet-ReadSXC
%define upstream_version 0.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Extract OpenOffice 1.x spreadsheet data
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Spreadsheet/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Zip)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch

%description
Spreadsheet::ReadSXC extracts data from OpenOffice 1.x spreadsheet files
(.sxc). It exports the function read_sxc() which takes a filename and an
optional reference to a hash of options as arguments and returns a
reference to a hash of references to two-dimensional arrays. The hash keys
correspond to the names of worksheets in the OpenOffice workbook. The
two-dimensional arrays correspond to rows and cells in the respective
spreadsheets. If you don't like this because the order of sheets is not
preserved in a hash, read on. The 'OrderBySheet' option provides an array
of hashes instead.

If you prefer to unpack the .sxc file yourself, you can use the function
read_xml_file() instead and pass the path to content.xml as an argument. Or
you can extract the XML string from content.xml and pass the string to the
function read_xml_string(). Both functions also take a reference to a hash
of options as an optional second argument.

Spreadsheet::ReadSXC requires XML::Parser to parse the XML contained in
.sxc files. Only the contents of text:p elements are returned, not the
actual values of table:value attributes. For example, a cell might have a
table:value-type attribute of "currency", a table:value attribute of
"-1500.99" and a table:currency attribute of "USD". The text:p element
would contain "-$1,500.99". This is the string which is returned by the
read_sxc() function, not the value of -1500.99.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.200.0-2mdv2011.0
+ Revision: 654295
- rebuild for updated spec-helper

* Tue Mar 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 521751
- import perl-Spreadsheet-ReadSXC


* Tue Mar 16 2010 cpan2dist 0.20-1mdv
- initial mdv release, generated with cpan2dist
