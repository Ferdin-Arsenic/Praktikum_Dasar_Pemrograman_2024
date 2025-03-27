module HitungBensin where
    hitungBensin :: Int -> Int -> Int 
    hitungRute :: Int -> Int

    hitungRute n 
        |n == 1 = 0
        |mod n 2 == 0 = 1 + hitungRute(div n 2)
        |otherwise = 1 + hitungRute(3*n +1)
    hitungBensin a b 
        | a == b = hitungRute a
        | otherwise = hitungRute a + hitungBensin (a+1) b

