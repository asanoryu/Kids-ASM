# Kids ASM

_Small educational REPL resembling an assembly like language for educational purposes_

Designed to be as simple as possible, using a few commands and only integer values.

## Registers:
Used as a tool to teach varibles.


        EAX, EBX - general purpose
        ERX - used as a temporary and result holder

## Commands:

* Move

    Put value in register

    _Examples_:

         Registers:
            <EAX: None>   <EBX: None>  <ERX: None>
        >>MOV 3 EAX
        Done
         Registers:
        <EAX: 3>   <EBX: None>  <ERX: None>

* Read

    Moves the value of register in ERX (works with EAX and EBX)


    _Examples_:

         Registers:
            <EAX: 3>   <EBX: None>  <ERX: None>
        >>READ EAX
        Done
         Registers:
        <EAX: 3>   <EBX: None>  <ERX: 3>



* Add

    Add value of register to ERX and store result in ERX


    _Examples_:

        Registers:
        <EAX: 3>   <EBX: None>  <ERX: 3>
        >>ADD EAX
        Done
        Registers:
        <EAX: 3>   <EBX: None>  <ERX: 6>

* Sub

    Subtracts value of EAX from ERX and stores result in ERX
    _Examples_:

        Registers:
        <EAX: 3>   <EBX: None>  <ERX: 6>
        >>SUB EAX
        Done
        Registers:
        <EAX: 3>   <EBX: None>  <ERX: 3>
