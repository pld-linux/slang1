%define		docver	1.4
Summary:    	shared library for C like extension language
Summary(de):	Shared Library für eine C-artige Sprache 
Summary(fr):	Bibliothèque partagée pour le langage d'extension C like
Summary(pl):	Biblioteka Slang
Summary(tr):	C benzeri dil için ortak kitaplýk
Name:      	slang
Version:   	1.3.5
Release:     	1
Serial:		1
Copyright:   	GPL
Group:       	Libraries
Group(pl):	Biblioteki
Source0:      	ftp://space.mit.edu/pub/davis/slang/%{name}%{version}.tar.gz
Source1:      	ftp://space.mit.edu/pub/davis/slang/%{name}%{docver}-doc.tar.gz
Patch0:		slang-security.patch
Patch1:		slang-keypad.1.patch
Buildroot:   	/tmp/%{name}-%{version}-root

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
%setup  -q -a1 -n %{name}%{version}
%patch0 -p1
%patch1 -p1 

%build
CFLAGS="$RPM_OPT_FLAGS" \
ELF_CFLAGS="$RPM_OPT_FLAGS -fPIC" \
LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--includedir=/usr/include/slang \
	--host=%{_host_alias} \
	--target=%{_target_platform}
	
make elf ELF_CFLAGS="$RPM_OPT_FLAGS -fPIC" CFLAGS="$RPM_OPT_FLAGS"
make all ELF_CFLAGS="$RPM_OPT_FLAGS -fPIC" CFLAGS="$RPM_OPT_FLAGS"
cd slsh
make DL_LIB="-ldl" ARCH="elf"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,src/examples/slang}

make install install-elf install-links \
	prefix=$RPM_BUILD_ROOT/usr \
	install_include_dir=$RPM_BUILD_ROOT/usr/include/slang
	
install -s slsh/slsh $RPM_BUILD_ROOT/usr/bin 

cp -a modules examples demo src/curses $RPM_BUILD_ROOT/usr/src/examples/slang

strip --strip-unneeded $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

gzip -9fn doc/sgml/* doc/*.txt 

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*.so.*.*
%attr(755,root,root) /usr/bin/*

%files devel
%defattr(644,root,root,755)
%doc doc/sgml/* doc/*.txt*
%doc /usr/src/examples/slang
/usr/lib/libslang.so
/usr/include/slang

%files static
%defattr(644,root,root,755)
/usr/lib/libslang.a

%changelog
* Wed May 12 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.3.5-1]
- upgrade to 1.3.5
- resync patches
- added sgml docs
- added examples and demos

* Sat Dec 12 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.2-2]
- added LDFLAGS="-s" to ./configure enviroment,
- added patch.slang-1.2.2.keypad.1 which
  prevents the Meta key from working with mutt (from mutt 0.95).

* Fri Aug 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.2-1]
- spec rewrited for using Buildroot,
- added %clean section,
- added using %%{name} in Source,
- added static subpackage,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added stripping shared libraries,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Fri Jun 26 1998 Alan Cox <alan@redhat.com>
- Swat another hole. Open TERMINFO files as the real uid not the euid.

* Fri Jun 26 1998 Alan Cox <alan@redhat.com>
- There's a hole in my library Dear Red Hat Dear Red Hat
- Squashed an sprintf arbitary length string into a small bufferon error
  bug.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 18 1998 Erik Troan <ewt@redhat.com>
- rebuilt to find terminfo in /usr/share

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Sep 1 1997 Donnie Barnes <djb@redhat.com>
- upgraded to 0.99.38 (will it EVER go 1.0???)
- all patches removed (all appear to be in this version)

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
