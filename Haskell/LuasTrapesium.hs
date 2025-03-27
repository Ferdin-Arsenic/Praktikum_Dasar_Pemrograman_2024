module LuasTrapesium where
    --Definisi dan Spesifikasi
    luasTrapesium :: Float ->  Float -> Float -> Float
    luasTrapesium t s1 s2 = 0.5 * t * (s1 + s2)
    