### RPM external libunwind 1.8.1-master
%define tag f081cf42917bdd5c428b77850b473f31f81767cf
%define branch master
Source0: git://github.com/%{n}/%{n}.git?obj=%{branch}/%{tag}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}-%{tag}.tgz

BuildRequires: autotools gmake
Requires: zlib xz

%prep
%setup -n %{n}-%{realversion}

%build
autoreconf -fiv
./configure CFLAGS="-g -O3 -fcommon" \
  CPPFLAGS="-I${ZLIB_ROOT}/include -I${XZ_ROOT}/include" \
  LDFLAGS="-L${ZLIB_ROOT}/lib -L${XZ_ROOT}/lib" \
  --prefix=%{i} --disable-block-signals --enable-zlibdebuginfo --disable-per-thread-cache
make %{makeprocesses}

%install

make %{makeprocesses} install
[ -d %{i}/lib64 ] && mv %{i}/lib64 %{i}/lib
%define drop_files %{i}/share/man %{i}/lib/pkgconfig %{i}/lib/*.a
