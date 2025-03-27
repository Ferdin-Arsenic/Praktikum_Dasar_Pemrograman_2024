module ListOfInteger where
    -- Definisi dan Spesifikasi
isMember :: [Int] -> Int -> Bool
isMember l1 i 
    |null l1 = False
    |head l1 == i = True
    |otherwise = isMember (tail l1) i
isEqual :: [Int] -> [Int] -> Bool
isEqual l1 l2 = l1 == l2
maxi :: [Int] -> Int
maxi li 
    |null li = 0
    |head li < maxi (tail li)  = maxi (tail li)
    |otherwise = head li
maxNb :: [Int] -> (Int, Int)
maxNb li = (maxi li, nbX (maxi li) li)
minList :: [Int] -> Int
{- minList l mengembalikan nilai minimum dari seluruh elemen list -}

nbX :: Int -> [Int] -> Int

{- nbX x l menghasilkan banyaknya kemunculan x pada l -}

jmlMin :: [Int] -> (Int,Int)

{- jmlMin l menghasilkan tuple (a,b) dengan:
      a adalah nilai minimum dari elemen-elemen l dan
      b adalah jumlah kemunculan a pada l -}
minList li 
    |length li == 1 = head li
    |head li < minList (tail li) = head li
    |otherwise = minList (tail li)
nbX x l 
    |null l = 0
    |head l == x = 1 + (nbX x (tail l))
    |otherwise = nbX x (tail l)
jmlMin li = (minList li, nbX (minList li) li)