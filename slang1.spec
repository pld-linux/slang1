#
# Conditional build:
%bcond_with	uClibc	# use hacks to build against uClibc
%bcond_with	utf8	# utf8 support
#
%define		docver	1.4.8
Summary:	shared library for C like extension language
Summary(de.UTF-8):   Shared Library für eine C-artige Sprache
Summary(es.UTF-8):   Biblioteca compartida para leguaje de extensión semejante a C
Summary(fr.UTF-8):   Bibliothèque partagée pour le langage d'extension C like
Summary(pl.UTF-8):   Biblioteka Slang
Summary(pt_BR.UTF-8):   Biblioteca compartilhada para linguagem de extensão semelhante a C
Summary(ru.UTF-8):   Разделяемая библиотека C-подобного языка расширения S-Lang
Summary(tr.UTF-8):   C benzeri dil için ortak kitaplık
Summary(uk.UTF-8):   Бібліотека спільного користування C-подібної мови розширення S-Lang
Name:		slang1
Version:	1.4.9
Release:	0.2%{?with_utf8:utf8}
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	ftp://space.mit.edu/pub/davis/slang/v1.4/slang-%{version}.tar.bz2
# Source0-md5:	4fbb1a7f1257e065ca830deefe13d350
Source1:	ftp://space.mit.edu/pub/davis/slang/v1.4/slang-%{docver}-doc.tar.bz2
# Source1-md5:	7dac82b282494affcf619730bbee0d6c
Patch0:		%{name}-security.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-nodevel.patch
Patch3:		%{name}-uclibc_ac_fix.patch
Patch4:		%{name}-remove_unused_terminfo_paths.patch
Patch5:		%{name}-cc.patch
Patch6:		%{name}-uClibc.patch
# utf8 patches: http://www.suse.de/~nadvornik/slang/
Patch7:		%{name}-debian-utf8.patch
Patch8:		%{name}-utf8-acs.patch
Patch9:		%{name}-utf8-fix.patch
URL:		http://www.s-lang.org/
BuildRequires:	autoconf
BuildRequires:	automake
Provides:	slang = %{epoch}:%{version}-%{release}
Obsoletes:	libslang1
Obsoletes:	slang < 2.0.0
%{?with_utf8:Provides: slang(utf8)}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/slang1

%description
Slang (pronounced ``sssslang'') is a powerful stack based interpreter
that supports a C-like syntax. It has been designed from the beginning
to be easily embedded into a program to make it extensible. Slang also
provides a way to quickly develop and debug the application embedding
it in a safe and efficient manner. Since slang resembles C, it is easy
to recode slang procedures in C if the need arises.

%description -l de.UTF-8
Slang (sprich ``sssslang'') ist ein leistungsfähiger stapelbasierter
Interpreter, der eine C-ähnliche Syntax unterstützt. Er kann auf
einfache Weise in ein Programm eingebettet werden, damit dieses
erweiterbar wird. Slang bietet außerdem eine Möglichkeit zum schnellen
Entwickeln und Debuggen der Anwendung, in die er eingebettet ist. Da
Slang C ähnlich ist, können Slang-Vorgänge einfach in C umgeschrieben
werden.

%description -l es.UTF-8
Slang (se pronuncia "sssslang") es un potente interpretador que
soporta C-como sintaxis. Fue escrito en el inicio para ser fácilmente
embutido en un programa para volverlo más extensible. Slang también
nos ofrece una manera de rápidamente desarrollar y depurar
aplicaciones, empotrándolo de manera segura y eficiente. Desde que
slang se parece a C, se hizo fácil recodificar los procedimientos
slang en C, si hace falta.

%description -l fr.UTF-8
slang (prononcez « sssslang ») est un interpréteur puissant offrant
une syntaxe à la C. Il a été conçu au début pour être facilement
intégré dans un programme afin de le rendre extensible. slang offre
aussi le moyen de developper et débugger rapidement l'application
intégrée de façon sûre et efficace. Comme slang ressemble à C, il est
facile de recoder les procédures slang en C si besoin est.

%description -l pl.UTF-8
Slang jest opartą o terminfo biblioteką do obsługi terminali
znakowych, posiadającą wbudowany interpreter języka podobnego
składniowo do C. Na początku był on przeznaczony aby łatwo dał się
osadzać w aplikację i uczynić ją rozszerzoną. Slang zapewnia
mechanizmy ułatwiające szybkie tworzenie rozbudowanych, łatwo
konfigurowalnych aplikacji. Slang również umożliwia proste
prześledzenie ewentualnych błędów w aplikacjach w bezpieczny i wydajny
sposób.

%description -l pt_BR.UTF-8
Slang (pronuncía-se "sssslang") é um poderoso interpretador que
suporta C-como sintaxe. Ele foi escrito no início para ser facilmente
embutido em um programa para torná-lo mais extensível. Slang também
oferece uma maneira de rapidamente desenvolver e depurar aplicações,
embutindo-o de maneira segura e eficiente. Desde que slang
assemelhou-se com C, tornou-se fácil re-codificar os procedimentos
slang em C se necessário.

%description -l ru.UTF-8
Slang - это мощный стековый интерпретатор, поддерживающий C-подобный
синтаксис. С самого начала он разрабатывался так, чтобы его можно было
легко встраивать в программы, делая их расширяемыми. Slang также дает
возможность быстрой разработки и отладки программ посредством
безопасного и эффективного встраивания в эти программы. Так как Slang
напоминает C, то при возникновении такой потребности, можно достаточно
легко перекодировать все процедуры slang в C.

%description -l tr.UTF-8
Slang, C'ye benzer bir yazımı olan, güçlü, yığın-tabanlı bir
yorumlayıcıdır. C'ye benzer olduğundan Slang ile yazılmış kodları C'ye
çevirmek oldukça kolaydır.

%description -l uk.UTF-8
Slang - це потужний стековий інтерпретатор, що підтримує C-подібний
синтаксис. З самого початку він розроблявся так, щоб його можна було
легко вбудовувати в програми, роблячи їх розширюваними. Slang також
дає можливість швидкої розробки та відлагоджування програм завдяки
безпечному та ефективному вбудовуванню в ці програми. Slang нагадує C,
так що, при виникненні такої потреби, можливо досить легко
перекодувати всі процедури Slang в C.

%package devel
Summary:	header files for slang C like language
Summary(de.UTF-8):   Header-Dateien für eine Slangvariante der C-Sprache
Summary(es.UTF-8):   Biblioteca y archivos de inclusión para slang
Summary(fr.UTF-8):   En-têtes pour le langage slang
Summary(pl.UTF-8):   Pliki nagłówkowe dla slanga
Summary(pt_BR.UTF-8):   Bibliotecas e arquivos de inclusão para slang
Summary(ru.UTF-8):   Библиотеки и хедеры для C-подобного языка S-Lang
Summary(tr.UTF-8):   slang dili için statik kitaplık ve başlık dosyaları
Summary(uk.UTF-8):   Бібліотеки та хедери для C-подібної мови S-Lang
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	slang-devel = %{epoch}:%{version}-%{release}
%{?with_utf8:Requires: slang(utf8)}
%{?with_utf8:Provides: slang-devel(utf8)}
Obsoletes:	libslang1-devel
Obsoletes:	slang-devel < 2.0.0

%description devel
This package contains header files required to develop slang-based
applications. It also includes documentation to help you write
slang-based apps.

%description devel -l de.UTF-8
Dieses Paket enthält Header-Dateien zum Entwickeln von slang-basierten
Anwendungen. Dokumentation zum Schreiben von slang-basierten
Anwendungen ist enthalten.

%description devel -l es.UTF-8
Este paquete contiene las bibliotecas y archivos de inclusión slang,
necesarios al desarrollo de aplicaciones basadas en slang.

%description devel -l fr.UTF-8
Ce paquetage contient les bibliothèques statiques et les en-têtes
slang pour développer des applications en slang. Il contient aussi la
documentation pour vous aider à écrire ces applications.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe slang. Znajduje się tutaj również
dokumentacja, która pomoże Ci w pisaniu aplikacji pod tę bibliotekę.

%description devel -l pt_BR.UTF-8
Este pacote contém as bibliotecas e arquivos de inclusão slang,
necessárias ao desenvolvimento de aplicações baseadas em slang.

%description devel -l ru.UTF-8
Этот пакет содержит библиотеки и хедеры, необходимые для разработки
программ, использующих Slang.

%description devel -l tr.UTF-8
Bu paket slang tabanlı uygulamalar geliştirmek için gereken başlık
dosyaları ve kitaplıkların yanısıra slang yardım belgelerini de
içerir.

%description devel -l uk.UTF-8
Цей пакет містить бібліотеки та хедери, необхідні для розробки
програм, що використовують Slang.

%package static
Summary:	slang static library
Summary(pl.UTF-8):   Biblioteka statyczna slang
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolvimento com slang
Summary(ru.UTF-8):   Статическая библиотека для C-подобного языка S-Lang
Summary(uk.UTF-8):   Статична бібліотека для C-подібної мови S-Lang
Group:		Development/Libraries
Provides:	slang-static = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
%{?with_utf8:Requires: slang-devel(utf8)}
%{?with_utf8:Provides: slang-static(utf8)}
Obsoletes:	slang-static < 2.0.0

%description static
This package contains the slang static libraries.

%description static -l de.UTF-8
Dieses Paket enthält die statischen Libraries.

%description static -l pl.UTF-8
Biblioteka statyczna slang.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com slang.

%description static -l ru.UTF-8
Этот пакет содержит статическую библиотеку, необходимую для разработки
программ, использующих Slang.

%description static -l uk.UTF-8
Цей пакет містить статичну бібліотеку, необхідну для розробки програм,
що використовують Slang.

%prep
%setup -q -n slang-%{version} -a1
%patch0 -p1
#%%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%{?with_uClibc:%patch6 -p1}
%if %{with utf8}
%patch6 -p1
%patch7 -p1
%patch8 -p1
%endif

%build
cp /usr/share/automake/config.sub autoconf
mv -f autoconf/aclocal.m4 acinclude.m4
mv -f autoconf/configure.in .
%{__aclocal}
%{__autoconf}
cd demo
cp -f ../acinclude.m4 .
%{__aclocal}
%{__autoconf}
cd ..
%configure

%{__make} elf \
	ELF_CFLAGS="%{rpmcflags} -fPIC"
%{__make} all \
	CFLAGS="%{rpmcflags}"

%{?with_utf8:ln -s libslang-utf8.so.%{version} src/elfobjs/libslang.so}

%{__make} -C slsh \
	DL_LIB="-ldl" \
	ARCH="elf" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-elf \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-links \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with utf8}
ln -sf libslang-utf8.so.%{version} ${RPM_BUILD_ROOT}%{_libdir}/libslang-utf8.so.1
ln -sf libslang-utf8.so ${RPM_BUILD_ROOT}%{_libdir}/libslang.so
ln -sf libslang-utf8.a ${RPM_BUILD_ROOT}%{_libdir}/libslang.a
%endif
mv $RPM_BUILD_ROOT%{_libdir}/libslang{,1}.so

install slsh/slsh $RPM_BUILD_ROOT%{_bindir}/slsh1

cp -a modules examples demo src/curses $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# help rpmdeps
chmod +x $RPM_BUILD_ROOT%{_libdir}/lib*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_libdir}/libslang1.so
%{_includedir}
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libslang*.a
