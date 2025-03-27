module KonversiSuhu where
    -- Definisi dan Spesifikasi
    konversiSuhu :: Float -> Char -> Float
    konversiSuhu x y
        | y == 'R' || y == 'r' = x * 4/5
        | y == 'K' || y == 'k' = x + 273.15
        | y == 'F' || y == 'f' = (x * 9/5) + 32


