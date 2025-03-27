module SumKelipatanX where
    sumKelipatanX :: Int -> Int -> Int -> Int
    sumKelipatanX m n x 
        |(m > n) = 0
        |(m <= n) && (mod m x == 0) = m + sumKelipatanX (m+1) n x
        |(m <= n) && (mod m x /= 0) = sumKelipatanX (m+1) n x 
        