"""
Mając na wejściu tablicę liczb, sprawdź czy istnieje taka
para identycznych liczb, których odległość między ich indeksami w tablicy jest
mniejsza lub równa k. Zwróć liczbe dla której różnica ta jest najmniejsza,
jak taka liczba nie istnieje to zwróć -1.
Przykłady 
arr = [1,2,3,5,2,4], k = 3; wynik = true -> (indeksy dla ‘2’, abs(1 - 4) == 3) 
arr = [1,2,3,4,5,1], k = 2; wynik = false (indeksy dla ‘1’, abs(0 - 5) > 2) 
arr = [1, 0, 1, 2, 2, 3, 0, 3], k = 2; wynik = true (dla ‘1’, ‘2’, ‘3’, różnica równa 1)
"""
  
      
def solution (arr, k):
	s = set()
	for i in range(k):
		s.add(arr[i])
	for i in range(len(arr)-k):
		if len(s)==k:
			s.add(arr[i+k])
			s.remove(arr[i])
		else:
			return True	
	return False 
	
	
def solution2 (arr,k):
	d =dict()
	min = 134129843649
	s=-1
	for i in range(len(arr)):
		if arr[i] in d:
			o= i-d[arr[i]]
			if o< min :
				min = o
				if min<=k:
					s=arr[i]
			d[arr[i]]= i
		else:
			d[arr[i]]= i
	return s

	
arr1 = [1,2,3,5,2,4]
arr2 = [1,2,3,4,5,1]
arr3 = [1, 0, 1, 2, 2, 3, 0, 3]
print( solution(arr1, 3))
print( solution(arr2, 2))


print( solution2(arr3,2))
print( solution2(arr2, 2))
