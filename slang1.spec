%define		docver	1.4
Summary:    	shared library for C like extension language
Summary(de):	Shared Library für eine C-artige Sprache 
Summary(fr):	Bibliothèque partagée pour le langage d'extension C like
Summary(pl):	Biblioteka Slang
Summary(tr):	C benzeri dil için ortak kitaplýk
Name:      	slang
Version:   	1.3.8
Release:     	1
Serial:		1
Copyright:   	GPL
Group:       	Libraries
Group(pl):	Biblioteki
Source0:      	ftp://space.mit.edu/pub/davis/slang/%{name}-%{version}.tar.bz2
Source1:      	ftp://space.mit.edu/pub/davis/slang/%{name}%{docver}-doc.tar.gz
Patch0:		slang-security.patch
Patch1:		slang-keypad.1.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Slang (pronounced ``sssslang'') is a powerful stack based interpreter that
supports a C-like syntax.  It has been designed from the beginning to be
easily embedded into a program to make it extensible. Slang also provides a
way to quickly develop and debug the application embedding it in a safe and
efficient manner.  Since slang resembles C, it is easy to recode slang
procedures in C if the need arises.

%description -l de
Slang (sprich ``sssslang'') ist ein leistungsfähiger stapelbasierter Interpreter,
der eine C-ähnliche Syntax unterstützt. Er kann auf einfache Weise in ein
Programm eingebettet werden, damit dieses erweiterbar wird. Slang bietet
außerdem eine Möglichkeit zum schnellen Entwickeln und Debuggen der 
Anwendung, in die er eingebettet ist. Da Slang C ähnlich ist, können
Slang-Vorgänge einfach in C umgeschrieben werden.

%description -l fr
slang (prononcez « sssslang ») est un interpréteur puissant offrant une
syntaxe à la C. Il a été conçu au début pour être facilement intégré dans
un programme afin de le rendre extensible. slang offre aussi le moyen de
developper et débugger rapidement l'application intégrée de façon sûre et
efficace. Comme slang ressemble à C, il est facile de recoder les procédures
slang en C si besoin est.

%description -l pl
Slang jest opart± o terminfo bibliotek± do obs³ugi terminali znakowych,
posiadaj±c± wbudowany interpreter jêzyka podobnego sk³adniowo do C.
Na pocz±tku by³ on przeznaczony aby ³atwo da³ siê osadzaæ w aplikacjê i
uczyniæ j± rozszerzon±. Slang zapewnia mechanizmy u³atwiaj±ce szybkie
tworzenie rozbudowanych, ³atwo konfigurowalnych aplikacji. Slang równie¿
umo¿liwia proste prze¶ledzenie ewentualnych b³êdów w aplikacjach w
bezpieczny i wydajny sposób.

%description -l tr
Slang, C'ye benzer bir yazýmý olan, güçlü, yýðýn-tabanlý bir yorumlayýcýdýr.
C'ye benzer olduðundan Slang ile yazýlmýþ kodlarý C'ye çevirmek oldukça
kolaydýr.

%package devel
Summary:   	header files for slang C like language
Summary(de):	Header-Dateien für eine Slangvariante der C-Sprache 
Summary(fr):	En-têtes pour le langage slang
Summary(pl):	Pliki nag³ówkowe dla slanga
Summary(tr):	slang dili için statik kitaplýk ve baþlýk dosyalarý
Group:       	Development/Libraries
Group(pl):   	Programowanie/Biblioteki
Requires:    	%{name} = %{version}

%description devel
This package contains header files required to develop slang-based
applications.  It also includes documentation to help you write slang-based
apps.

%description -l de devel
Dieses Paket enthält Header-Dateien zum Entwickeln von slang-basierten
Anwendungen. Dokumentation zum Schreiben von slang-basierten Anwendungen ist
enthalten.

%description -l pl devel
Pakiet ten zawiera pliki nag³ówkowe slang. Znajduje siê tutaj
równie¿ dokumentacja, która pomo¿e Ci w pisaniu aplikacji pod
ta bibliotekê.

%description -l fr devel
Ce paquetage contient les bibliothèques statiques et les en-têtes
slang pour développer des applications en slang. Il contient aussi
la documentation pour vous aider à écrire ces applications.

%description -l tr devel
Bu paket slang tabanlý uygulamalar geliþtirmek için gereken baþlýk dosyalarý
ve kitaplýklarýn yanýsýra slang yardým belgelerini de içerir.

%package static
Summary:     	slang static library
Summary(pl): 	Biblioteka statyczna slang
Group:       	Development/Libraries
Group(pl):   	Programowanie/Biblioteki
Requires:    	%{name}-devel = %{version}

%description static
This package contains the slang static libraries.

%description -l de static
Dieses Paket enthält die statischen Libraries.

%description -l pl static
Biblioteka statyczna slang.

%prep
%setup  -q -a1
%patch0 -p1
%patch1 -p1 

%build
LDFLAGS="-s" \
./configure %{_target} \
	--prefix=%{_prefix} \
	--includedir=%{_includedir}/slang
	
make elf ELF_CFLAGS="$RPM_OPT_FLAGS -fPIC" CFLAGS="$RPM_OPT_FLAGS"
make all ELF_CFLAGS="$RPM_OPT_FLAGS -fPIC" CFLAGS="$RPM_OPT_FLAGS"
cd slsh
make DL_LIB="-ldl" ARCH="elf"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/src/examples/slang,%{_bindir}}

make install install-elf install-links \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	install_include_dir=$RPM_BUILD_ROOT%{_includedir}/slang
	
install -s slsh/slsh $RPM_BUILD_ROOT%{_bindir} 

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

cp -a modules examples demo src/curses $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

gzip -9fn doc/sgml/* doc/*.txt 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/sgml/* doc/*.txt*

%attr(755,root,root) %{_libdir}/libslang.so
%{_includedir}/slang

%{_prefix}/src/examples/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libslang.a
