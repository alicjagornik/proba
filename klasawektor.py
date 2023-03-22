import random
import math

class Vector:

    def __init__(self,v,a):
        '''
        funkcja __init__:
        funkcja konstruuje wektor o podanych w tablicy wspolrzednych i wymiarze
        input:
        v-tablica zawiera wspolrzedne wektora
        a-int wymiar wektora
        output:
        brak
        '''
        self.a=a
        self.v=v

    def losowa_generacja(self):
        '''
        funkcja losowa_generacja:
        funkcja losuje calkowite wspolrzedne wektora z przedzialu od 0 do 9
        input:
        brak
        output:
        self.v - tab otrzymujemy losowe wspolrzedne wektora 
        '''
        for i in range(self.a):
            self.v[i]=random.randint(0,9)
        return self.v

    def wczytywanie(self,tab):
        '''
        funkcja wczytywanie:
        funkcja przypisuje wartosci podane jako argument do odpowiednich wspolrzednych wektora
        input:
        tab- tablica tablica z nowymi wartosciami
        output:
        self.v-tab otrzymujemy nowe wspolrzedne wektora
        '''
        for i in range(self.a):
            self.v[i]=tab[i]
        return self.v

    def __add__(self,other):
        '''
        funckja __add__:
        funckja za pomocą operatora + dodaje odpowiednie elementy dwóch wektorów
        input:
        self + other - tab obiekty które chcemy do siebie dodać
        output:
        self- tab nadpisany obiekt, który jest sumą wektorów
        lub "ValueError" pojawia się gdy rozmiary wektrów się nie zgadzają
        '''
        if self.a==other.a :
            for i in range(self.a):
                self.v[i]=self.v[i]+other.v[i]
            return self.v
        else: return "ValueError"

    def __sub__(self,other):
        '''
        funckja __sub__:
        funckja za pomocą operatora - odejmuje odpowiednie elementy dwóch wektorów
        input:
        self - other - tab obiekty które chcemy od siebie odjąć
        output:
        self- tab nadpisany obiekt, który jest różnicą wektorów
        lub "ValueError" pojawia się gdy rozmiary wektrów się nie zgadzają
        '''
        if self.a==other.a :
            for i in range(self.a):
                self.v[i]=self.v[i]-other.v[i]
            return self.v
        else: return "ValueError"

    def mnozenieprzezskalar(self,k):
        '''
        funkcja mnozenie:
        funkcja mnozy wektor przez skalar
        input:
        k- int skalar
        output:
        self.v-tab otrzymujemy wektor pomnozony przez skalar
        '''
        for i in range(self.a):
                self.v[i]=self.v[i]*k
        return self.v

    def dlugosc(self):
        '''
        funkcja dlugosc:
        funkcja liczy dlugosc wektora
        input:
        brak
        output:
        d-int dlugosc wektora
        '''
        d=0
        for i in range(self.a):
            d+=self.v[i]**2
        d=math.sqrt(d)
        return d

    def suma_elementow(self):
        '''
        funkcja suma_elementow:
        funkcja dodaje do siebie wspolrzedne wektora
        input:
        brak
        output:
        s- int suma wspolrzednych
        '''
        s=0
        for i in range(self.a):
            s+=self.v[i]
        return s

    def __mul__(self,other):
        '''
        funkcja __mul__:
        funkcja liczy iloczyn skalarny dwoch wektorow
        input:
        other- obiekt (wektor ktory chcemy pomnozyc skalarnie)
        output:
        l- int iloczyn skalarny wektorow 
        '''
        l=0
        for i in range(self.a):
            l+=self.v[i]*other.v[i]    
        return l

    def __contains__(self,t):
        '''
        funkcja __contains__
        zwraca True lub False jeśli element t znajduje jest elementem wektora
        input:
        t - int elemnet ktory chcemy sprawdzic czy jest w liscie
        output:
        True - jeśli element jest w wektorze
        False- jeśli nie ma elementu w wektorze
        '''
        if t in self.v: return True
        else: return False

    def __str__(self):
        '''
        funkcja __str__
        zwraca reprezentacje tekstowa wektora
        input:
        brak
        output:
        wektor
        '''
        return str(self.v)

    def __getitem__(self,p):
        '''
        funkcja __getitem__
        zwraca element ktory znajduje sie na podanej pozycji
        input:
        p - int pozycja ktora chcemy otrzymac
        output:
        element wektora, któy znajduje się na pozycji nr p
        '''
        return self.v[p-1]
