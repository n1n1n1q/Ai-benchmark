"""
Rational
"""
from math import gcd
from math import lcm
class Rational:
    """
    Rational number
    """
    def __init__(self, num, den) -> None:
        if den==0:
            raise ValueError("Denominator cannot be zero.")
        if num*den<=0:
            self.numerator=-abs(num)
            self.denominator=abs(den)
        else:
            self.numerator=num
            self.denominator=den
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    def reduce(self):
        """
        Reduce rational
        >>> Rational(2,6).reduce()
        "1/3"
        """
        tmp_gcd=gcd(self.denominator,self.numerator)
        return Rational(self.numerator//tmp_gcd,self.denominator//tmp_gcd)

    def __add__(self,other):
        tmp_lcm=lcm(self.denominator,other.denominator)
        tmp = Rational(self.numerator*(tmp_lcm//self.denominator)+
                    other.numerator*(tmp_lcm//other.denominator),tmp_lcm).reduce()
        return tmp

    def __sub__(self,other):
        tmp_lcm=lcm(self.denominator,other.denominator)
        tmp= Rational(self.numerator*(tmp_lcm//self.denominator)-
                    other.numerator*(tmp_lcm//other.denominator),tmp_lcm).reduce()
        return tmp

    def __mul__(self,other):
        return Rational(self.numerator*other.numerator,self.denominator*other.denominator).reduce()

    def __truediv__(self,other):
        return Rational(self.numerator*other.denominator,self.denominator*other.numerator).reduce()

    def __eq__(self,other):
        self_reduced=self.reduce()
        other_reduced=other.reduce()
        return self_reduced.denominator==other_reduced.denominator \
    and self_reduced.numerator==other_reduced.numerator

    def __lt__(self,other):
        return self.numerator/self.denominator<other.numerator/other.denominator

    def __le__(self,other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self,other):
        return not self.__lt__(other)

    def __ge__(self,other):
        return self.__gt__(other) or self.__eq__(other)

    @property
    def mixed_form(self):
        """
        Rational's mixed form
        """
        if self.numerator%self.denominator==0:
            return str(self.numerator//self.denominator)
        tmp=f'{abs(self.numerator)//self.denominator} \
{abs(self.numerator)-abs(abs(self.numerator)//self.denominator*self.denominator)}\
/{self.denominator}'
        if tmp[0:2]=="0 ":
            tmp=tmp[2:]
        return tmp if self.numerator>=0 else "-"+tmp

    @mixed_form.setter
    def mixed_form(self,new):
        if len(new.split(' '))==1:
            self.numerator=int(new.split('/')[0])
            self.denominator=int(new.split('/')[1])
        elif new[0]=='-':
            tmp=new.split(' ')
            self.numerator=-(abs(int(tmp[0]))*int(tmp[1].split('/')[1])+\
                             abs(int(tmp[1].split('/')[0])))
            self.denominator=int(tmp[1].split('/')[1])
        else:
            tmp=new.split(' ')
            self.numerator=int(tmp[0])*int(tmp[1].split('/')[1])+int(tmp[1].split('/')[0])
            self.denominator=int(tmp[1].split('/')[1])
