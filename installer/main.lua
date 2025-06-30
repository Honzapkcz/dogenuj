package.path = "share/?.lua;share/?/init.lua"
package.cpath = "lib/?/core.so;lib/?.so"
local term = require("terminal")
local http = require("socket.http")
local lfs = require("lfs")

local function dump(t)
    for k, v in pairs(t) do
        print(tostring(k)..": "..tostring(v))
    end
end

http.USERAGENT = "Kujnuj/2.3.1 (honzapkcz)"

-- local body, code, headers = http.request("https://srv.hbmc.net/MODPACKVERSION")

local sbox = term.draw.box_fmt.single
local depth = 0

function table_longest(t)
    local l = 0
    for _, v in ipairs(t) do
        l = (#v > l) and #v or l
    end
    return l
end

function string_split(str, sep)
    sep = sep or "\n"
    local t = {}
    for s in string.gmatch(str, "([^"..sep.."]*)") do
        table.insert(t, s)
    end
    return t
end

function popup_yesno(title, question)
    local y, x = 2 + depth * 2, 2 + depth * 4
    depth = depth + 1
    question = string_split(question)
    term.cursor.position.set(y, x)
    term.draw.box(#question + 5, table_longest(question) + 4, sbox, true, title)
    for i, v in ipairs(question) do
        term.cursor.position.set(y + i, 2 + x)
        term.output.print(v)
    end
    term.cursor.position.set(#question + 2 + y, 1 + x)
    term.draw.line.horizontal(table_longest(question) + 2)
    term.cursor.position.set(#question + 3 + y, 2 + x)
    term.output.print("Y - Yes  N - No")
    depth = depth - 1
    while true do
        local c = term.input.readansi(1)
        if c == "y" then
            return true
        elseif c == "n" then
            return false
        end
    end
end

function popup_message(title, message)
    local y, x = 2 + depth * 2, 2 + depth * 4
    depth = depth + 1
    message = string_split(message)
    term.cursor.position.set(y, x)
    term.draw.box(#message + 5, table_longest(message) + 4, sbox, true, title)
    for i, v in ipairs(message) do
        term.cursor.position.set(i + y, 2 + x)
        term.output.print(v)
    end
    term.cursor.position.set(#message + 2 + y, 1 + x)
    term.draw.line.horizontal(table_longest(message) + 2)
    term.cursor.position.set(#message + 3 + y, 2 + x)
    term.output.print("Any to OK")
    depth = depth - 1
    term.input.readansi(9999)
end

local function main_redraw()
    local h, w = term.size()
    term.clear.screen()
    term.cursor.position.set(1, 1)
    term.draw.box(h, w, term.draw.box_fmt.single, nil, nil, true)
    term.output.flush()
end

local function main()
    main_redraw()
    local yn = popup_yesno("Question?", "Is this good enough popup?\nI hope so...\n\nHehehehe\nGetting delighted\noogabooga")
    main_redraw()
    if yn then
        popup_message("Message", "Thank you...")
    else
        popup_message("Message", "Fuck you...")
    end
end

term.initwrap(main, {displaybackup = true, filehandle = io.stdout})()