shopt -s globstar
./luastatic "$1.lua"    \
    share/**/*.lua      \
    lib/**/*.so         \
    /lib/liblua.so      \
    -I/usr/include/
if [ -n "$2" ]; then
    "./$1"
fi
