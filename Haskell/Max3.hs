module Max3 where 
    max3 :: Int -> Int -> Int -> Int
    max3 a b c 
        | c > b && c > a = c
        | b > a = b 
        |otherwise = a
