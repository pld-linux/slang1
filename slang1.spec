%define		docver  1.4
Summary:	shared library for C like extension language
Summary(de):	Shared Library für eine C-artige Sprache 
Summary(fr):	Bibliothèque partagée pour le langage d'extension C like
Summary(pl):	Biblioteka Slang
Summary(tr):	C benzeri dil için ortak kitaplık
Name:		slang
Version:	1.4.4
Release:	7
Epoch:		1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
Source0:	ftp://space.mit.edu/pub/davis/slang/v1.4/%{name}-%{version}.tar.bz2
Source1:	ftp://space.mit.edu/pub/davis/slang/v1.4/%{name}%{docver}-doc.tar.gz
Patch0:		%{name}-security.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-nodevel.patch
Patch3:		%{name}-keymap.patch
%{?BOOT:BuildRequires:	uClibc-devel-BOOT}
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/slang

%description
Slang (pronounced ``sssslang'') is a powerful stack based interpreter
that supports a C-like syntax. It has been designed from the beginning
to be easily embedded into a program to make it extensible. Slang also
provides a way to quickly develop and debug the application embedding
it in a safe and efficient manner. Since slang resembles C, it is easy
to recode slang procedures in C if the need arises.

%description -l de
Slang (sprich ``sssslang'') ist ein leistungsfähiger stapelbasierter
Interpreter, der eine C-ähnliche Syntax unterstützt. Er kann auf
einfache Weise in ein Programm eingebettet werden, damit dieses
erweiterbar wird. Slang bietet außerdem eine Möglichkeit zum schnellen
Entwickeln und Debuggen der Anwendung, in die er eingebettet ist. Da
Slang C ähnlich ist, können Slang-Vorgänge einfach in C umgeschrieben
werden.

%description -l fr
slang (prononcez « sssslang ») est un interpréteur puissant offrant
une syntaxe à la C. Il a été conçu au début pour être facilement
intégré dans un programme afin de le rendre extensible. slang offre
aussi le moyen de developper et débugger rapidement l'application
intégrée de façon sûre et efficace. Comme slang ressemble à C, il est
facile de recoder les procédures slang en C si besoin est.

%description -l pl
Slang jest opart± o terminfo bibliotek± do obs³ugi terminali
znakowych, posiadaj±c± wbudowany interpreter jêzyka podobnego
sk³adniowo do C. Na pocz±tku by³ on przeznaczony aby ³atwo da³ siê
osadzaæ w aplikacjê i uczyniæ j± rozszerzon±. Slang zapewnia
mechanizmy u³atwiaj±ce szybkie tworzenie rozbudowanych, ³atwo
konfigurowalnych aplikacji. Slang równie¿ umo¿liwia proste
prze¶ledzenie ewentualnych b³êdów w aplikacjach w bezpieczny i wydajny
sposób.

%description -l tr
Slang, C'ye benzer bir yazımı olan, güçlü, yığın-tabanlı bir
yorumlayıcıdır. C'ye benzer olduğundan Slang ile yazılmış kodları C'ye
çevirmek oldukça kolaydır.

%package devel
Summary:	header files for slang C like language
Summary(de):	Header-Dateien für eine Slangvariante der C-Sprache 
Summary(fr):	En-têtes pour le langage slang
Summary(pl):	Pliki nag³ówkowe dla slanga
Summary(tr):	slang dili için statik kitaplık ve başlık dosyaları
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
This package contains header files required to develop slang-based
applications. It also includes documentation to help you write
slang-based apps.

%description devel -l de
Dieses Paket enthält Header-Dateien zum Entwickeln von slang-basierten
Anwendungen. Dokumentation zum Schreiben von slang-basierten
Anwendungen ist enthalten.

%description devel -l fr
Ce paquetage contient les bibliothèques statiques et les en-têtes
slang pour développer des applications en slang. Il contient aussi la
documentation pour vous aider à écrire ces applications.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe slang. Znajduje siê tutaj równie¿
dokumentacja, która pomo¿e Ci w pisaniu aplikacji pod tê bibliotekê.

%description devel -l tr
Bu paket slang tabanlı uygulamalar geliştirmek için gereken başlık
dosyaları ve kitaplıkların yanısıra slang yardım belgelerini de
içerir.

%package static
Summary:	slang static library
Summary(pl):	Biblioteka statyczna slang
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
This package contains the slang static libraries.

%description static -l de
Dieses Paket enthält die statischen Libraries.

%description static -l pl
Biblioteka statyczna slang.

%package devel-BOOT
Summary:	Static slang for bootdisk
Summary(pl):	Statyczny slang dla bootkietki
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ

%description devel-BOOT
Static slang for bootdisk (compiled against uClibc headers).

%description devel-BOOT -l pl
Statyczny slang dla bootkietki (skompilowany z nag³ówkami uClibc).

%prep
%setup  -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
(cd autoconf ; mv -f acsite.m4 aclocal.m4 ; autoconf ; cp -f configure ..)
(cd demo ; cp -f ../autoconf/aclocal.m4 . ; autoconf)
%configure

%if %{?BOOT:1}%{!?BOOT:0}
# BOOT version
%{__make} all \
	CFLAGS="-m386 -Os -fno-strength-reduce -I%{_libdir}/bootdisk/usr/include" \
	OTHERSTUFF=""
mv -f src/objs/libslang.a libslang.a-BOOT
%{__make} clean
%endif

# normal
%{__make} elf ELF_CFLAGS="%{rpmcflags} -fPIC"
%{__make} all CFLAGS="%{rpmcflags}"
%{__make} -C slsh DL_LIB="-ldl" ARCH="elf" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_bindir}}

%if %{?BOOT:1}%{!?BOOT:0}
# BOOT version
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk%{_libdir}
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk%{_includedir}
install libslang.a-BOOT $RPM_BUILD_ROOT%{_libdir}/bootdisk%{_libdir}/libslang.a
install src/slang.h src/slcurses.h $RPM_BUILD_ROOT%{_libdir}/bootdisk%{_includedir}
%endif

%{__make} install install-elf install-links \
	DESTDIR=$RPM_BUILD_ROOT
	
install slsh/slsh $RPM_BUILD_ROOT%{_bindir} 

cp -a modules examples demo src/curses $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf doc/sgml/* doc/*.txt 

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html doc/*.gz
%attr(755,root,root) %{_libdir}/libslang.so
%{_includedir}
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libslang.a

%if %{?BOOT:1}%{!?BOOT:0}
%files devel-BOOT
%defattr(644,root,root,755)
%{_libdir}/bootdisk%{_libdir}/*.a
%{_libdir}/bootdisk%{_includedir}
%endif
