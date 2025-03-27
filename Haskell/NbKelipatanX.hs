module NbKelipatanX where
--Definisi dan Spesifikasi
nbKelipatanX :: Int -> Int -> Int -> Int
nbKelipatanX m n x   
    |m == n = 
        if mod n x == 0 then 1
        else 0
    |mod n x == 0 = 1 + nbKelipatanX m (n-1) x
    |otherwise = 0 + nbKelipatanX m (n-1) x
