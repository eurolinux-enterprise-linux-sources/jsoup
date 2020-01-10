Name:           jsoup
Version:        1.6.1
Release:        10%{?dist}
Summary:        Java library for working with real-world HTML

License:        MIT

URL:            http://%{name}.org/

# git clone git://github.com/jhy/jsoup
# git archive --prefix="jsoup-1.6.1/" --format=tar jsoup-1.6.1 | xz > jsoup-1.6.1.tar.xz
Source0:        %{name}-%{version}.tar.xz

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: maven-local
BuildRequires: maven-source-plugin
BuildRequires: maven-plugin-plugin


%description
jsoup is a Java library for working with real-world HTML.
It provides a very convenient API for extracting and manipulating data,
using the best of DOM, CSS, and jquery-like methods.

jsoup implements the WHATWG HTML5 specification,
and parses HTML to the same DOM as modern browsers do.

 - scrape and parse HTML from a URL, file, or string
 - find and extract data, using DOM traversal or CSS selectors
 - manipulate the HTML elements, attributes, and text
 - clean user-submitted content against a safe white-list,
   to prevent XSS attacks
 - output tidy HTML

jsoup is designed to deal with all varieties of HTML found in the wild;
from pristine and validating, to invalid tag-soup;
jsoup will create a sensible parse tree.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README CHANGES

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.6.1-10
- Mass rebuild 2013-12-27

* Fri Aug 16 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6.1-9
- Migrate away from mvn-rpmbuild (#997437)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.1-8
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.6.1-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 04 2012 Jaromir Capik <jcapik@redhat.com> - 1.6.1-4
- Removing maven from Requires

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Jaromir Capik <jcapik@redhat.com> - 1.6.1-2
- Switching to sources from github

* Fri Jul 22 2011 Jaromir Capik <jcapik@redhat.com> - 1.6.1-1
- Initial package
