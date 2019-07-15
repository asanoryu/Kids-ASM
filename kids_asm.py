"""A mini ASM type toy languange for educational purposes."""

import click
from typing import Optional, List


class Register:
    """All registers in kids_asm."""

    def __init__(self, name: str):
        """Initialize value of the register."""
        self.value: Optional[int] = None
        self.name: str = name

    def __repr__(self):
        """Nice repr for the REPL.
        
        <EAX : 2>
        """
        return f"<{self.name}: {self.value}>"


class Parser:
    """Main parser that will hold the main REPL."""

    def __init__(self):
        """Initialize all registers.
        
        EAX, EBX - general purpose registers.
        ERX - intermediate register for holding transitional values.

        Sets parsing map.
        """
        self.eax = Register("EAX")
        self.ebx = Register("EBX")
        self.erx = Register("ERX")

        self.parse_map = {
            "mov": self._mov,
            "add": self._add,
            "sub": self._sub,
            "read": self._read,
        }

        self.reg_map = {"erx": self.erx, "eax": self.eax, "ebx": self.ebx}

    def parse(self, input_: str):
        """Parse current input and passes it to eval part."""
        parts = input_.lower().split()
        print(self.parse_map[parts[0]](parts[1:]))

    def _mov(self, params: List) -> str:
        """Move value to register.
        
        Either an int value or the value of an register.
        Ex.:
        MOV 3,EAX - puts 3 in EAX
        MOV ERX, EAX - puts whatever value ERX has to EAX
        """
        if len(params) < 2:
            return f"Error: Not enough parameters - expected 2 got {len(params)}"
        val = params[0].strip(",")
        reg = params[1]
        if reg not in ("erx", "ebx", "eax"):
            return f"Error: MOV expects second parameter to be the name of a register! got {val}"
        try:
            val = int(val)
            self.reg_map[reg].value = val
        except ValueError:
            if val not in ("erx", "eax", "ebx"):
                return f"Error: MOV expects first parameter to be an integer or name of a register! got {val}"
            self.reg_map[reg].value = self.reg_map[val].value
        return "Done"

    def _add(self, param: List) -> str:
        param = param[0]
        if param not in ("ebx", "eax"):
            return f"Error: ADD expects parameter to be either EAX or EBX! got {param}"
        if self.reg_map[param].value is None or self.erx.value is None:
            return f"Error: Cannot add empty values"
        self.erx.value = self.erx.value + self.reg_map[param].value
        return "Done"

    def _sub(self, param: List) -> str:
        param = param[0]
        if param not in ("ebx", "eax"):
            return f"Error: ADD expects parameter to be either EAX or EBX! got {param}"
        if self.reg_map[param].value is None or self.erx.value is None:
            return f"Error: Cannot substract empty values"
        self.erx.value = self.erx.value - self.reg_map[param].value
        return "Done"

    def _read(self, param: List) -> str:
        param = param[0]
        if param not in ("ebx", "eax"):
            return f"Error: READ expects parameter to be either EAX or EBX! got {param}"
        if self.reg_map[param].value is None:
            return f"Error: Cannot READ empty value in {param}"
        self.erx.value = self.reg_map[param].value
        return "Done"

    def __repr__(self):
        """Dump all registers for debug."""
        return f"Registers: \n {self.eax}   {self.ebx}  {self.erx}"


@click.command()
def repl():
    """Start REPL for Kids_ASM."""
    kasm = Parser()
    print("Welcome to Kids ASM")
    print("=" * 60)
    while True:

        print(f"{kasm}")
        inp = input(">>")
        kasm.parse(inp)
    pass


if __name__ == "__main__":
    repl()
