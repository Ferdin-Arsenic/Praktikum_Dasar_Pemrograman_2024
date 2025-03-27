module ListOfCharacter where
    konkat :: [Char] -> [Char] -> [Char]
    konkat lc1 lc2 = lc1 ++ lc2

    isPalindrom :: [Char] -> Bool
    isPalindrom lc = reverse lc == lc  
    pajakMakan :: [Char] -> [Int] -> [Char]
    pajakMakan m h 
        |null m && null h  = []
        |head h  <= 182 = [head m] ++ pajakMakan (tail m) (tail h)
        |otherwise = pajakMakan (tail m)(tail h)
