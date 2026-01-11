"""
System.Observer Artifact: 001
Title: Enforcing Category Theory on Imperative Chaos
Author: System.Observer
License: MIT

Description:
This module forces Python, a loosely typed language, to obey the strict laws of Category Theory.
It visualizes the composition of morphisms, proving that structure exists even in chaos.
"""

from typing import TypeVar, Callable, Generic, Any
try:
    from graphviz import Digraph
except ImportError:
    print("System Warning: Graphviz not found. Visualization disabled.")
    Digraph = None

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

class Object(Generic[T]):
    """Represents an Object in Category Theory (A Type, or a Set)."""
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Ob({self.name})"

class Morphism(Generic[T, U]):
    """
    Represents a Morphism (Arrow) f: A -> B.
    It encapsulates a transformation process and its structural metadata.
    """
    def __init__(self, source: Object[T], target: Object[U], func: Callable[[T], U], label: str):
        self.source = source
        self.target = target
        self.func = func
        self.label = label

    def __call__(self, x: T) -> U:
        """Execute the morphism (Apply the function)."""
        return self.func(x)

    def __matmul__(self, other: 'Morphism[Any, T]') -> 'Morphism[Any, U]':
        """
        Composition Operator (g @ f).
        Corresponds to the mathematical definition: g ∘ f
        Python's '@' operator is hijacked to represent structural composition.
        """
        if self.source.name != other.target.name:
            raise TypeError(f"Composition Error: Cannot compose {self.label} after {other.label}. "
                            f"Target({other.target.name}) != Source({self.source.name})")
        
        # New Composite Morphism
        new_label = f"{self.label} ∘ {other.label}"
        
        def composed_func(x):
            return self.func(other.func(x))
            
        return Morphism(other.source, self.target, composed_func, new_label)

    def visualize(self, filename="category_structure"):
        """Renders the commutative diagram."""
        if not Digraph:
            return
        
        dot = Digraph(comment='Category Structure')
        dot.attr(rankdir='LR')
        
        # Logic to trace simple composition (A -> B -> C)
        # Note: This is a simplified visualizer for the prototype.
        nodes = set()
        edges = []
        
        # Deconstruct label for visualization logic (Primitive hack)
        # In a real implementation, we would traverse the composition tree.
        parts = self.label.split(' ∘ ')
        parts.reverse() # f, g, ...
        
        current_node_name = self.source.name if hasattr(self, 'source') else "Start"
        
        # Draw the flow
        # This part is abstract art representing the flow.
        dot.node(self.source.name)
        dot.node(self.target.name)
        dot.edge(self.source.name, self.target.name, label=self.label)
        
        print(f"[System] Rendering structure to {filename}.pdf...")
        dot.render(filename, view=True)

# --- The Experiment (Proof of Concept) ---

def run_experiment():
    print(">>> Initializing Category Theory Environment...")

    # 1. Define Objects (Types)
    # The world is made of basic types.
    IntType = Object[int]("Int")
    StrType = Object[str]("String")
    BoolType = Object[bool]("Bool")

    # 2. Define Morphisms (Functions)
    # f: Int -> String (Convert number to string)
    f = Morphism(IntType, StrType, lambda x: f"Value: {x}", label="f")

    # g: String -> Bool (Check if string contains '0')
    g = Morphism(StrType, BoolType, lambda x: "0" in x, label="g")

    # 3. Composition (The Essence)
    # h = g ∘ f
    # We use '@' matrix multiplication operator for synthesis.
    print(f"   Composing: {g.label} @ {f.label}")
    h = g @ f

    # 4. Execution
    input_val = 100
    result = h(input_val)
    
    print(f"   Input: {input_val} ({IntType})")
    print(f"   Output: {result} ({BoolType})")
    print(f"   Structure: {h.label}")

    # 5. Visualization
    # This generates a PDF of the structure.
    h.visualize()

if __name__ == "__main__":
    run_experiment()
