module JamBangun where
--Definisi dan Spesifikasi
banguntelat :: Int -> Int -> Int -> Bool
banguntelat j m d 
    |j > 31 = False
    |j <= 31 && m > 45 = False
jamBangun :: Int -> Int -> Int -> (Bool, Int, Int, Int)
jamBangun j m d =
    let 
        bangunsec = 3600*7 + 60*45
        dosensec = 3600*j + 60*m + d
        selisihsec 
            |bangunsec > dosensec = bangunsec- dosensec
            |otherwise = dosensec - bangunsec

        selisihjam = div selisihsec 3600
        selisihmenit = div (mod selisihsec 3600) 60
        selisihdetik = mod selisihsec 60

    in 
        (bangunsec > dosensec, selisihjam, selisihmenit, selisihdetik)