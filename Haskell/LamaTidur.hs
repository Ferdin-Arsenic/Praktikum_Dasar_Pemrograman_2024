module LamaTidur where
    lamaTidur :: Int -> Int -> Int -> (Bool, Int, Int, Int)
    lamaTidur j m d =
        let
            waktu1 = 3600 * j + m * 60 + d 
            waktu2 = 3600 * 5

            selisih 
                | j < 5 = waktu2 - waktu1
                | otherwise = waktu2 - waktu1 + 24 *3600

            jam = div selisih 3600
            menit = div (mod selisih 3600) 60
            detik = mod selisih 60

            cukup = jam >= 6
        in
            (cukup, jam, menit, detik)