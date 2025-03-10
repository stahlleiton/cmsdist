### RPM external gosamcontrib 2.0-20150803
Source: http://www.hepforge.org/archive/gosam/gosam-contrib-%{realversion}.tar.gz

Requires: qgraf
Requires: form

%define keep_archives true

%prep
%setup -q -n gosam-contrib-2.0

%build
CXX="$(which c++) -fPIC"
CC="$(which gcc) -fPIC"
FC="$(which gfortran) -std=legacy"
PLATF_CONF_OPTS="--enable-shared --enable-static"

./configure $PLATF_CONF_OPTS \
            --prefix=%i \
            --bindir=%i/bin \
%ifarch riscv64
            --build=%{_arch}-unknown-linux-gnu \
%endif
            --libdir=%i/lib \
            CXX="$CXX" CC="$CC" FC="$FC" F77="${FC}"

make %makeprocesses all

%install
make install
rm %{i}/lib/*.la

%post
%{relocateConfig}share/gosam-contrib/gosam.conf
