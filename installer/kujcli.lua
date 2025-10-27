#!/usr/bin/lua

local splash = string.gsub([[
\e[32m█| █|█|  █|    █|█|  █|█|  █|    █|\e[0m
\e[32m█|█| █|  █|    █|██| █|█|  █|    █|\e[0m
\e[32m██|  █|  █|    █|█|█|█|█|  █|    █|\e[0m
\e[32m█|█| █|  █|█|  █|█| ██|█|  █|█|  █|\e[0m
\e[32m█| █|█████|█████|█|  █|█████|█████|\e[0m
\e[32mMinecraft Kujnuj instalační skript\e[0m
]], "\\e", "\27")

lfs_unix = {
	cwd = function ()
		--TODO: use io.popen()
		--return os.execute('pwd')
	end,
	chdir = function (path)
		return os.execute('cd '..path)
	end,
	list = function (path)
		local ls, err = io.popen(̈́'ls -1 '..path..'"', "r")
		if err then
			return nil, err
		end
		local t = {}
		for s in string.gmatch("([^\n]*)") do
			t[#t+1] = s
		end
		return s
	end,
	mkdir = function (name)
		return os.execute('mkdir "'..name)
	end,
	rmdir = function (path)
		return os.remove(path)
	end,
	remove = function(path)
		return os.execute('rm -rf "'..path..'"')
	end,
	copy = function (src, dest)
		return os.execute('cp -r "'..src..'" "'..dest..'"')
	end
}

lfs_nt = {} --TODO
-- TODO: linux/windows check
if true then
	lfs = lfs_unix
else
	lfs = lfs_nt
end

local version = "KUJNUJ 2.3.1"
local useragent = "Kujnuj/2.3.1 (honzapkcz)"
local upstream = "https://srv.hbmc.net/MODPACKVERSION"
local cwd = lfs.cwd()

print(splash)
