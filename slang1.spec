%define		docver  1.4
Summary:	shared library for C like extension language
Summary(de):	Shared Library fЭr eine C-artige Sprache
Summary(es):	Biblioteca compartida para leguaje de extensiСn semejante a C
Summary(fr):	BibliothХque partagИe pour le langage d'extension C like
Summary(pl):	Biblioteka Slang
Summary(pt_BR):	Biblioteca compartilhada para linguagem de extensЦo semelhante a C
Summary(ru):	Разделяемая библиотека C-подобного языка расширения S-Lang
Summary(tr):	C benzeri dil iГin ortak kitaplЩk
Summary(uk):	Б╕бл╕отека сп╕льного користування C-под╕бно╖ мови розширення S-Lang
Name:		slang
Version:	1.4.5
Release:	4
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	ftp://space.mit.edu/pub/davis/slang/v1.4/%{name}-%{version}.tar.bz2
Source1:	ftp://space.mit.edu/pub/davis/slang/v1.4/%{name}%{docver}-doc.tar.gz
Patch0:		%{name}-security.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-nodevel.patch
Patch3:		%{name}-uclibc_ac_fix.patch
Patch4:		%{name}-remove_unused_terminfo_paths.patch
Patch5:		%{name}-cc.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libslang1

%define		_includedir	%{_prefix}/include/slang

%description
Slang (pronounced ``sssslang'') is a powerful stack based interpreter
that supports a C-like syntax. It has been designed from the beginning
to be easily embedded into a program to make it extensible. Slang also
provides a way to quickly develop and debug the application embedding
it in a safe and efficient manner. Since slang resembles C, it is easy
to recode slang procedures in C if the need arises.

%description -l de
Slang (sprich ``sssslang'') ist ein leistungsfДhiger stapelbasierter
Interpreter, der eine C-Дhnliche Syntax unterstЭtzt. Er kann auf
einfache Weise in ein Programm eingebettet werden, damit dieses
erweiterbar wird. Slang bietet auъerdem eine MЖglichkeit zum schnellen
Entwickeln und Debuggen der Anwendung, in die er eingebettet ist. Da
Slang C Дhnlich ist, kЖnnen Slang-VorgДnge einfach in C umgeschrieben
werden.

%description -l es
Slang (se pronuncia "sssslang") es un potente interpretador que
soporta C-como sintaxis. Fue escrito en el inicio para ser fАcilmente
embutido en un programa para volverlo mАs extensible. Slang tambiИn
nos ofrece una manera de rАpidamente desarrollar y depurar
aplicaciones, empotrАndolo de manera segura y eficiente. Desde que
slang se parece a C, se hizo fАcil recodificar los procedimientos
slang en C, si hace falta.

%description -l fr
slang (prononcez ╚ sssslang ╩) est un interprИteur puissant offrant
une syntaxe Ю la C. Il a ИtИ conГu au dИbut pour Йtre facilement
intИgrИ dans un programme afin de le rendre extensible. slang offre
aussi le moyen de developper et dИbugger rapidement l'application
intИgrИe de faГon sШre et efficace. Comme slang ressemble Ю C, il est
facile de recoder les procИdures slang en C si besoin est.

%description -l pl
Slang jest opart╠ o terminfo bibliotek╠ do obsЁugi terminali
znakowych, posiadaj╠c╠ wbudowany interpreter jЙzyka podobnego
skЁadniowo do C. Na pocz╠tku byЁ on przeznaczony aby Ёatwo daЁ siЙ
osadzaФ w aplikacjЙ i uczyniФ j╠ rozszerzon╠. Slang zapewnia
mechanizmy uЁatwiaj╠ce szybkie tworzenie rozbudowanych, Ёatwo
konfigurowalnych aplikacji. Slang rСwnie© umo©liwia proste
prze╤ledzenie ewentualnych bЁЙdСw w aplikacjach w bezpieczny i wydajny
sposСb.

%description -l pt_BR
Slang (pronuncМa-se "sssslang") И um poderoso interpretador que
suporta C-como sintaxe. Ele foi escrito no inМcio para ser facilmente
embutido em um programa para tornА-lo mais extensМvel. Slang tambИm
oferece uma maneira de rapidamente desenvolver e depurar aplicaГУes,
embutindo-o de maneira segura e eficiente. Desde que slang
assemelhou-se com C, tornou-se fАcil re-codificar os procedimentos
slang em C se necessАrio.

%description -l ru
Slang - это мощный стековый интерпретатор, поддерживающий C-подобный
синтаксис. С самого начала он разрабатывался так, чтобы его можно было
легко встраивать в программы, делая их расширяемыми. Slang также дает
возможность быстрой разработки и отладки программ посредством
безопасного и эффективного встраивания в эти программы. Так как Slang
напоминает C, то при возникновении такой потребности, можно достаточно
легко перекодировать все процедуры slang в C.

%description -l tr
Slang, C'ye benzer bir yazЩmЩ olan, gЭГlЭ, yЩПЩn-tabanlЩ bir
yorumlayЩcЩdЩr. C'ye benzer olduПundan Slang ile yazЩlmЩЧ kodlarЩ C'ye
Гevirmek oldukГa kolaydЩr.

%description -l uk
Slang - це потужний стековий ╕нтерпретатор, що п╕дтриму╓ C-под╕бний
синтаксис. З самого початку в╕н розроблявся так, щоб його можна було
легко вбудовувати в програми, роблячи ╖х розширюваними. Slang також
да╓ можлив╕сть швидко╖ розробки та в╕длагоджування програм завдяки
безпечному та ефективному вбудовуванню в ц╕ програми. Slang нагаду╓ C,
так що, при виникненн╕ тако╖ потреби, можливо досить легко
перекодувати вс╕ процедури Slang в C.

%package devel
Summary:	header files for slang C like language
Summary(de):	Header-Dateien fЭr eine Slangvariante der C-Sprache
Summary(es):	Biblioteca y archivos de inclusiСn para slang
Summary(fr):	En-tЙtes pour le langage slang
Summary(pl):	Pliki nagЁСwkowe dla slanga
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo para slang
Summary(ru):	Библиотеки и хедеры для C-подобного языка S-Lang
Summary(tr):	slang dili iГin statik kitaplЩk ve baЧlЩk dosyalarЩ
Summary(uk):	Б╕бл╕отеки та хедери для C-под╕бно╖ мови S-Lang
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libslang1-devel

%description devel
This package contains header files required to develop slang-based
applications. It also includes documentation to help you write
slang-based apps.

%description devel -l de
Dieses Paket enthДlt Header-Dateien zum Entwickeln von slang-basierten
Anwendungen. Dokumentation zum Schreiben von slang-basierten
Anwendungen ist enthalten.

%description devel -l es
Este paquete contiene las bibliotecas y archivos de inclusiСn slang,
necesarios al desarrollo de aplicaciones basadas en slang.

%description devel -l fr
Ce paquetage contient les bibliothХques statiques et les en-tЙtes
slang pour dИvelopper des applications en slang. Il contient aussi la
documentation pour vous aider Ю Иcrire ces applications.

%description devel -l pl
Pakiet ten zawiera pliki nagЁСwkowe slang. Znajduje siЙ tutaj rСwnie©
dokumentacja, ktСra pomo©e Ci w pisaniu aplikacji pod tЙ bibliotekЙ.

%description devel -l pt_BR
Este pacote contИm as bibliotecas e arquivos de inclusЦo slang,
necessАrias ao desenvolvimento de aplicaГУes baseadas em slang.

%description devel -l ru
Этот пакет содержит библиотеки и хедеры, необходимые для разработки
программ, использующих Slang.

%description devel -l tr
Bu paket slang tabanlЩ uygulamalar geliЧtirmek iГin gereken baЧlЩk
dosyalarЩ ve kitaplЩklarЩn yanЩsЩra slang yardЩm belgelerini de
iГerir.

%description devel -l uk
Цей пакет м╕стить б╕бл╕отеки та хедери, необх╕дн╕ для розробки
програм, що використовують Slang.

%package static
Summary:	slang static library
Summary(pl):	Biblioteka statyczna slang
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com slang
Summary(ru):	Статическая библиотека для C-подобного языка S-Lang
Summary(uk):	Статична б╕бл╕отека для C-под╕бно╖ мови S-Lang
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains the slang static libraries.

%description static -l de
Dieses Paket enthДlt die statischen Libraries.

%description static -l pl
Biblioteka statyczna slang.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com slang.

%description static -l ru
Этот пакет содержит статическую библиотеку, необходимую для разработки
программ, использующих Slang.

%description static -l uk
Цей пакет м╕стить статичну б╕бл╕отеку, необх╕дну для розробки програм,
що використовують Slang.

%prep
%setup  -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
mv -f autoconf/aclocal.m4 acinclude.m4
mv -f autoconf/configure.in .
%{__aclocal}
%{__autoconf}
cd demo
	cp -f ../acinclude.m4 .
	aclocal
	autoconf
cd ..
%configure

%{__make} elf ELF_CFLAGS="%{rpmcflags} -fPIC"
%{__make} all CFLAGS="%{rpmcflags}"
%{__make} -C slsh DL_LIB="-ldl" ARCH="elf" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_bindir}}

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
