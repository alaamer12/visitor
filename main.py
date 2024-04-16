from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Element interface
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

# Concrete elements
class ConcreteElementA(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_element_a(self)

    def operation_a(self) -> str:
        return "Operation A"

class ConcreteElementB(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_element_b(self)

    def operation_b(self) -> str:
        return "Operation B"

# Visitor interface
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element: ConcreteElementA) -> None:
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element: ConcreteElementB) -> None:
        pass

# Concrete visitors
class ConcreteVisitor1(Visitor):
    def visit_concrete_element_a(self, element: ConcreteElementA) -> None:
        print(f"{element.operation_a()} visited by ConcreteVisitor1")

    def visit_concrete_element_b(self, element: ConcreteElementB) -> None:
        print(f"{element.operation_b()} visited by ConcreteVisitor1")

class ConcreteVisitor2(Visitor):
    def visit_concrete_element_a(self, element: ConcreteElementA) -> None:
        print(f"{element.operation_a()} visited by ConcreteVisitor2")

    def visit_concrete_element_b(self, element: ConcreteElementB) -> None:
        print(f"{element.operation_b()} visited by ConcreteVisitor2")

# Object structure
class ObjectStructure:
    def __init__(self) -> None:
        self.elements: List[Element] = []

    def attach(self, element: Element) -> None:
        self.elements.append(element)

    def detach(self, element: Element) -> None:
        self.elements.remove(element)

    def accept(self, visitor: Visitor) -> None:
        for element in self.elements:
            element.accept(visitor)

# Usage
if __name__ == "__main__":
    object_structure = ObjectStructure()
    object_structure.attach(ConcreteElementA())
    object_structure.attach(ConcreteElementB())

    concrete_visitor1 = ConcreteVisitor1()
    concrete_visitor2 = ConcreteVisitor2()

    object_structure.accept(concrete_visitor1)
    object_structure.accept(concrete_visitor2)
