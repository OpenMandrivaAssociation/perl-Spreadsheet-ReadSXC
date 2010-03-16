%define upstream_name    Spreadsheet-ReadSXC
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Extract OpenOffice 1.x spreadsheet data
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Spreadsheet/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Archive::Zip)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::Parser)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


