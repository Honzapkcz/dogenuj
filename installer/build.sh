shopt -s globstar
./luastatic main.lua    \
    share/**/*.lua      \
    lib/**/*.so         \
    /lib/liblua.so      \
    -I/usr/include/
if [ -n "$1" ]; then
    ./main
fi