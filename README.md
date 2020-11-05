## What is it
That's a short script that generates the ZIP files with the correct naming convention for CG1.

## How to use it
Basic structe for the Script
```
CG1
├── cg1_exercise_00
│   ├── skeleton
│   │   ├── types
│   │   ├── src
│   │   ├── public
│   │   └── node_modules
│   └── cg1_ex0.pdf
│
├── cg1_exercise_01
│   ├── skeleton
│   │   └── ... 
│   └── cg1_ex0.pdf
│
├── cg1_exercise_02 
│   └── ...
.
.
.
├── cg1_exercise_XX
│   └── ...
.
.
.
└── cg1_exercise_NN
    └── ...
```

Just change ``firstName``, ``lastName`` and ``path`` in
```
do(firstName="Max", lastName="Mustermann", path=".")
```

## Note

Notice that everytime you run this script, every ZIP is newly generated.

## Disclaimer

I do not assume liability for errors contained in or for damages arising from the use of this software. 