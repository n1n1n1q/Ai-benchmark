"mo duli"

from typing import Any


class Mono:
    """Mono class"""

    def __init__(self, coefficient: int, degree: int, next_=None) -> None:
        self.coefficient = coefficient
        if not coefficient:
            self.degree = 0
        else:
            self.degree = degree
        self.next = next_

    def __str__(self) -> str:
        output = "Mono: "
        if not self.coefficient or self.degree == 0:
            return output + str(self.coefficient)

        if self.coefficient not in (1, -1):
            output += str(self.coefficient)

        if self.coefficient == -1:
            output += "-"

        if self.degree == 1:
            return output + "x"
        return output + f"x**{self.degree}"

    def __repr__(self) -> str:
        return f"Mono(coeff={self.coefficient}, degree={self.degree})"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Mono):
            return self.degree == other.degree and self.coefficient == other.coefficient
        return False


class Polynomial:
    """Polynomial class"""

    def __init__(self, *args: list[Mono]) -> None:
        if isinstance(args[0], Polynomial):
            self.head = args[0].head
            curr = self.head
            while curr.next is not None:
                curr = curr.next
        else:
            self.head = Mono(args[0].coefficient, args[0].degree)
            curr = self.head
        for mono in args[1:]:
            if isinstance(mono, Polynomial):
                second = mono.head
                while second is not None:
                    curr.next = Mono(second.coefficient, second.degree)
                    curr = curr.next
                    second = second.next
            else:
                curr.next = Mono(mono.coefficient, mono.degree)
                curr = curr.next

    def __str__(self):
        polynom = ""

        curr = self.head

        if (
            curr is not None and not curr.coefficient and curr.next is None
        ) or not curr:
            return "Polynomial: 0"

        # chat gpt found error in my code
        tmp_curr = self.head
        ind = True

        while tmp_curr is not None:
            if tmp_curr.coefficient:
                ind = False
                break
            tmp_curr = tmp_curr.next

        if ind:
            return "Polynomial: 0"

        while curr is not None:
            if curr.coefficient > 0 and polynom:
                polynom += "+"

            if curr.coefficient:
                polynom += str(curr).split()[1]

            curr = curr.next

        return "Polynomial: " + polynom

    def __repr__(self) -> str:
        output = "Polynomial("

        curr = self.head
        while curr is not None:
            output += repr(curr)
            if curr.next is not None:
                output += " -> "
            curr = curr.next

        return output + ")"

    @property
    def degree(self):
        """returns largest power"""
        degree = 0
        curr = self.head
        while curr is not None:
            degree = max(degree, curr.degree)
            curr = curr.next
        return degree

    def copy(self) -> "Polynomial":
        """copies polynom"""
        if not self.head:
            return Polynomial(Mono(0, 0))

        new_head = Polynomial(Mono(self.head.coefficient, self.head.degree))
        # new_head = copy(self.head)
        new_curr = new_head.head
        curr = self.head.next
        while curr is not None:
            new_curr.next = Mono(curr.coefficient, curr.degree)
            new_curr = new_curr.next
            curr = curr.next

        return new_head

    def sort(self) -> None:
        """
        destructive method
        sorts a polynom in a descending order
        """

        curr = self.head

        while curr and curr.next is not None:
            second = curr.next
            while second is not None:
                if second.degree > curr.degree:
                    tmp = curr.coefficient, curr.degree
                    curr.coefficient, curr.degree = second.coefficient, second.degree
                    second.coefficient, second.degree = tmp
                second = second.next

            curr = curr.next

        curr = self.head

        while curr and curr.next is not None:
            if not curr.degree and not curr.next.degree and not curr.coefficient:
                curr.coefficient = curr.next.coefficient
                curr.next.coefficient = 0

            curr = curr.next

    def simplify(self):
        """simplifies given polyomial"""
        while self.head is not None and not self.head.coefficient:
            self.head = self.head.next

        first = self.head
        while first is not None and first.next is not None:
            second = first
            while second is not None and second.next is not None:
                if second.next.degree == first.degree:
                    first.coefficient += second.next.coefficient
                    second.next = second.next.next
                else:
                    second = second.next
            first = first.next

        first = self.head

        if first and first.next is None and not first.coefficient:
            self.head = None
            return

        while first is not None and first.next is not None:
            if not first.next.coefficient:
                first.next = first.next.next
            else:
                first = first.next

    def eval_at(self, val: int | float) -> int | float:
        """evaluates a polynomial at a certain point"""
        res = 0
        curr = self.head
        while curr is not None:
            res += curr.coefficient * (val**curr.degree)
            curr = curr.next

        return res

    def __eq__(self, other: Any):
        if isinstance(other, Polynomial):
            first = self.copy()
            second = other.copy()
            first.simplify()
            second.simplify()
            first.sort()
            second.sort()

            first = first.head
            second = second.head

            while first is not None and second is not None:
                if first != second:
                    return False

                first = first.next

                second = second.next

            if (first and second is None) or (second and first is None):
                return False

            return True

        return False

    def __hash__(self):
        new_polynom = self.copy()
        new_polynom.simplify()
        new_polynom.sort()

        return hash(str(new_polynom))

    @property
    def derivative(self) -> "Polynomial":
        """returns a derivative"""
        derivative = self.copy()

        while derivative.head.degree == 1:
            derivative.head = derivative.head.next

        curr = derivative.head

        while curr is not None:
            curr.coefficient *= curr.degree
            curr.degree -= 1
            curr = curr.next

        derivative.simplify()

        return derivative

    def __add__(self, other: "Polynomial") -> "Polynomial":
        new_polynomial = self.copy()
        # first = new_polynomial.head
        second = other.head

        while second is not None:

            new_polynomial.head = Mono(
                second.coefficient, second.degree, new_polynomial.head
            )
            second = second.next

        new_polynomial.simplify()
        new_polynomial.sort()

        return new_polynomial

    def __sub__(self, other: "Polynomial") -> "Polynomial":
        new_polynomial = self.copy()
        # first = new_polynomial.head
        second = other.head

        while second is not None:

            new_polynomial.head = Mono(
                -second.coefficient, second.degree, new_polynomial.head
            )
            second = second.next

        new_polynomial.simplify()
        new_polynomial.sort()

        return new_polynomial

    def __mul__(self, other: "Polynomial") -> "Polynomial":
        if isinstance(other, Polynomial):
            new_polynomial = Polynomial(Mono(0, 0))

            second = other.head
            while second is not None:
                tmp_polynomial = self.copy()
                curr = tmp_polynomial.head
                while curr is not None:
                    curr.coefficient *= second.coefficient
                    curr.degree += second.degree
                    curr = curr.next

                new_polynomial += tmp_polynomial
                second = second.next
        elif isinstance(other, int):
            new_polynomial = self.copy()
            curr = new_polynomial.head

            while curr is not None:
                curr.coefficient *= other
                curr = curr.next

        return new_polynomial

    def __rmul__(self, other: "Polynomial") -> "Polynomial":
        return self.__mul__(other)
