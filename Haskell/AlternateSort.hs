module AlternateSort where
alternateSort :: [Int] -> [Int]

sortL :: [Int] -> [Int]
minList :: [Int] -> Int
delMin :: [Int] -> Int -> [Int]

minList li 
    |length li == 1 = head li
    |head li < minList (tail li) = head li
    |otherwise = minList (tail li)

delMin li x  
    |null li = []
    |head li == x = tail li
    |otherwise = [head li] ++ delMin(tail li) x

sortL li 
    |null li = []
    |otherwise = [minList li] ++ sortL (delMin li (minList li))

alternateSort li 
    | null (sortL li)|| length (sortL li)== 1 = li
    | otherwise = [head (sortL li), last (sortL li)] ++ alternateSort (tail (init (sortL li) ))
