package.path = "modules/share/?.lua;modules/share/?/init.lua"
package.cpath = "modules/lib/?/core.so;modules/lib/?.so"
local term = require("terminal")
local sock = require("socket")
local lfs = require("lfs")

local function dump(t)
    for k, v in pairs(t) do
        print(tostring(k)..": "..tostring(v))
    end
end

dump(term)
print()
dump(sock)
print()
dump(lfs)
print()
