module DeretSegitiga where
-- Definisi dan Spesifikasi
deretSegitiga :: Int -> Int
deretSegitiga n 
    |n == 1 = 1
    |otherwise = n + deretSegitiga (n-1) 